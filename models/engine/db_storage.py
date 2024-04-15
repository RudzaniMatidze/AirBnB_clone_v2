#!/usr/bin/python3
""" 
Handle a the details of how to connect to the SQL database and execute commands
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scope_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review

class DBStorage:
    """
     DBStorage class for managing database storage using SQLAlchemy.
    """
    __engine = None
    __session = None
    def __init__(self) -> None:
        """
        Initializes the DBStorage instance by creating the engine and session.
        """
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database_name = getenv("HBNB_MYSQL_DB")
        database_url = "mysql+mysqldb://{}:{}@{}/{}".format(username,
                                                            password,
                                                            host,
                                                            databse_name)
        self.__engine = create_engine(database_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries objects from the database based on class name.
        Returns a dictionary with object IDs as keys and objects as values.
        """
        obj_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
                if issubclass(cls, Base):
                    obj_list = self.__session.query(cls).all()
                else:
                    for subclass in Base.__subclasses__():
                        objs_list.extend(self.__session.query(subclass).all())
                obj_dict = {}
                for obj in objs_list:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    obj_dict[key] = obj
                return obj_dict

        def new(self, obj):
            """
            Adds the object to the current database session.
            """
            self.__session.ass(obj)
            self.__session.commit()

        def save(self):
            """
            Commits all changes to the current database session.
            """
            self.__session.commit()

        def delete(self, obj=None):
            """
            Deletes the object from the current database session.
            """
            if obj:
                self.__session.delete(obj)

        def reload(self):
            """
            Reloads the database session and recreates tables.
            """
            Base.metadata.drop_all(self.__engine)
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
