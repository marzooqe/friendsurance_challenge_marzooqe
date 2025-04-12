#!/usr/bin/env python

import logging
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


class DBConnector:
    def __init__(self, username, password, host, database, port):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.port = port
        self.engine = None
        logging.basicConfig(
            format="| %(process)d | %(levelname)s | %(message)s |", level=logging.INFO
        )

    def connect(self):
        url = f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        try:
            self.engine = create_engine(url, pool_recycle=3600)
            conn = self.engine.connect()
            time.sleep(1)  # Simulate some latency for connection establishment
            conn.close()
            logging.info("Database connection established.")
            return self.engine
        except SQLAlchemyError as e:
            logging.error(f"Database connection failed: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error during connection: {e}")
            raise
