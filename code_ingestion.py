import pandas as pd 
import os 
import time
from sqlalchemy import create_engine 
import psycopg2
import logging

''' Setting up logging info to log ingestion details. '''
logging.basicConfig(
    filename="logs/ingestion_db.log", 
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filemode="a"  
)


engine = create_engine("postgresql+psycopg2://postgres:aryan@localhost/crop_production")


''' This function ingests dataframes into the database table.'''
def ingest_db(df, table, engine):
    df.to_sql(table, engine, if_exists='replace', index=False)

''' This function loads csv files from the directories and ingests them into the database.'''
def load_raw_data():
    for file in os.listdir("data"):
        if '.csv' in file:
            start_time = time.time()
            df = pd.read_csv(f"data/{file}")
            print(f"{file} ->", df.shape)
            logging.info(f"ingesting {file} into database")
            ingest_db(df, file[:-4], engine)
            logging.info(f"ingested {file} into successfully")
            end_time = time.time()
            logging.info(f"Time taken to ingest is {end_time - start_time} seconds")

if __name__ == "__main__":
    load_raw_data()
    logging.info("All data ingested successfully")