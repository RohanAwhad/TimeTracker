import os
import pytest

from setup import setup_db_env_vars
from sqlalchemy import create_engine

setup_db_env_vars()
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

conn = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

def test_conn():
    engine = create_engine(conn)
    