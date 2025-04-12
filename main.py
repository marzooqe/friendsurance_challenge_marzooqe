#!/usr/bin/env python

import logging
import os
from dotenv import load_dotenv
from db_util.db_connect import DBConnector
from data_processing.csv_processing import load_csv_to_table

# Load environment variables from .env file
load_dotenv()


# Fetch environment variables with validation
def get_env_var(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Missing environment variable: {var_name}")
    return value


INPUT_DIR = get_env_var("INPUT_DIR")
POSTGRES_PASSWORD = get_env_var("POSTGRES_PASSWORD")
POSTGRES_USER = get_env_var("POSTGRES_USER")
POSTGRES_DB = get_env_var("POSTGRES_DB")
POSTGRES_HOST = get_env_var("POSTGRES_HOST")
POSTGRES_PORT = get_env_var("POSTGRES_PORT")


def main():
    try:
        # Connect to the database using credentials from environment variables
        connector = DBConnector(
            POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DB, POSTGRES_PORT
        )
        engine = connector.connect()

        # Load CSV files into respective tables
        load_csv_to_table(
            engine,
            "customer",
            os.path.join(INPUT_DIR, "customer.csv"),
            ["customer_id", "customer_country", "customer_age", "customer_gender"],
            "customer_id",  # Primary Key Column
        )

        load_csv_to_table(
            engine,
            "exchange_rate",
            os.path.join(INPUT_DIR, "exchange_rate.csv"),
            [
                "exchange_rate_id",
                "from_currency",
                "to_currency",
                "effective_date",
                "rate",
            ],
            "exchange_rate_id",  # Primary Key Column
        )

        load_csv_to_table(
            engine,
            "transaction_detail",
            os.path.join(INPUT_DIR, "transaction.csv"),
            [
                "transaction_detail_id",
                "customer_id",
                "transaction_type",
                "transaction_amount",
                "transaction_currency",
                "transaction_date",
            ],
            "transaction_detail_id",  # Primary Key Column
        )
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")
        raise


if __name__ == "__main__":
    main()
