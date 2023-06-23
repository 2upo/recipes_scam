"""Main program loop."""

from database import Database
from config import Config

class Main(object):
    """Main control loop."""

    def run(self):
        """Run program."""
        conf = Config()
        db = Database(
            conf.DATABASE_HOST,
            conf.DATABASE_USERNAME,
            conf.DATABASE_PASSWORD,
            conf.DATABASE_PORT,
            conf.DATABASE_NAME,
        )
        db.connect()
        cursor = db.conn.cursor()
        cursor.execute("SELECT 42")
        records = cursor.fetchall()
        print(records)
        return 0

if __name__ == "__main__":
    Main().run()