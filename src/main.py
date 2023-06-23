"""Main program loop."""

from database import Database
from config import Config

class Main(object):
    """Main control loop."""

    def run(self):
        """Run program."""
        conf = Config()
        db = Database()
        db.connect()
        cursor = db.conn.cursor()
        cursor.execute("SELECT 42")
        records = cursor.fetchall()
        print(records)
        return 0

if __name__ == "__main__":
    Main().run()