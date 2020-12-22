import os


def setup_db_env_vars():
    os.environ["DB_USER"] = "ronny_500"
    os.environ["DB_PASSWORD"] = "password"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_NAME"] = "TimeTracker"
