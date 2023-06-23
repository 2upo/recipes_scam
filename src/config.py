"""Load config from environment variables."""
from os import environ, path
from dotenv import load_dotenv


class Config(object):
    """Project-wide storage of configs."""

    # Load variables from .env
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

    # Database config
    DATABASE_HOST = environ.get("DATABASE_HOST")
    DATABASE_USERNAME = environ.get("DATABASE_USERNAME")
    DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
    DATABASE_PORT = environ.get("DATABASE_PORT")
    DATABASE_NAME = environ.get("DATABASE_NAME")

    # SQL queries
    SQL_QUERIES_FOLDER = "sql"

    # Client config
    TG_BOT_TOKEN = ""
    PASSPHRASE = "947a1d7c612299deb61ce23830ef239d4a53dbb7197bb69aa622f4967538f11e"
