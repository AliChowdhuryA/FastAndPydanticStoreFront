# app/database.py



# Replace with your actual database URL
from databases import Database


DATABASE_URL = "sqlite:///./test.db"  # or "postgresql://user:password@localhost/dbname"

database = Database(DATABASE_URL)
