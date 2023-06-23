"""Threadsafe singletone for PostgreSQL + Psycopg operations."""

from log import LOGGER
import psycopg2
import threading
from psycopg2.extras import DictCursor
from config import Config


class Database(object):
    """PostgreSQL Database class."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        conf = Config()
        self.host = conf.DATABASE_HOST
        self.username = conf.DATABASE_USERNAME
        self.password = conf.DATABASE_PASSWORD
        self.port = conf.DATABASE_PORT
        self.dbname = conf.DATABASE_NAME
        self.conn = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname,
                )
            except psycopg2.DatabaseError as e:
                LOGGER.error(e)
                raise e
            finally:
                LOGGER.info("Connection opened successfully.")
