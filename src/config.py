"""Load config from environment variables."""
from os import environ, path
from dotenv import load_dotenv


class Config(object):
    """Project-wide storage of configs."""

    # Load variables from .env
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

    # Database config
    DSN = environ.get("DSN")

    # Client config
    TG_BOT_TOKEN = environ.get("BOT_TOKEN")
    PASSPHRASE_HASH = environ.get("PASSPHRASE_HASH")
