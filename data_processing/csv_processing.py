#!/usr/bin/env python

import csv
import logging
import os
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import schema, text

logging.basicConfig(
    format="| %(process)d | %(levelname)s | %(message)s |", level=logging.INFO
)


def get_table(engine, table_name):
    metadata = schema.MetaData()
    try:
        table = schema.Table(table_name, metadata, autoload_with=engine)
        return table
    except SQLAlchemyError as e:
        logging.error(f"Error retrieving table {table_name}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error fetching table {table_name}: {e}")
        raise


def validate_csv_file(file_path):
    """Check if the CSV file exists and is readable."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"CSV file {file_path} does not exist.")
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"CSV file {file_path} is empty.")
    logging.info(f"CSV file {file_path} is valid.")


def load_csv_to_table(engine, table_name, file_path, columns, pk_column):
    """
    Load data from CSV to the database table with upsert functionality based on the primary key column.
    This uses raw SQL for PostgreSQL upsert.
    """
    validate_csv_file(file_path)
    table = get_table(engine, table_name)

    try:
        with engine.begin() as connection:
            with open(file_path, mode="r") as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # Skip header row
                rows = []
                for row in reader:
                    if len(row) == len(columns):  # Skip rows with invalid length
                        values = {col: row[idx] for idx, col in enumerate(columns)}
                        rows.append(values)
                    else:
                        logging.warning(f"Skipping invalid row: {row}")

                if rows:
                    # Perform the upsert operation using raw SQL with the 'ON CONFLICT' clause
                    for row in rows:
                        columns_str = ", ".join(row.keys())
                        values_str = ", ".join([f"'{v}'" for v in row.values()])
                        update_str = ", ".join(
                            [
                                f"{k} = EXCLUDED.{k}"
                                for k in row.keys()
                                if k != pk_column
                            ]
                        )

                        # Create the SQL query for upsert (ON CONFLICT)
                        upsert_sql = f"""
                        INSERT INTO {table_name} ({columns_str})
                        VALUES ({values_str})
                        ON CONFLICT ({pk_column}) 
                        DO UPDATE SET {update_str};
                        """

                        # Execute the upsert SQL
                        connection.execute(text(upsert_sql))

                    logging.info(
                        f"Upserted {len(rows)} rows into '{table_name}' from '{file_path}'."
                    )
                else:
                    logging.warning(
                        f"No valid data to load into '{table_name}' from '{file_path}'."
                    )

    except (SQLAlchemyError, FileNotFoundError, IndexError) as e:
        logging.error(f"Failed loading CSV into '{table_name}': {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error loading CSV into '{table_name}': {e}")
        raise
