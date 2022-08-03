import os
from utils.db_utils import create_db_engine, run_query, insert_data
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists

DATA_PATH = os.path.join('data', 'vetclinic_procedures.parquet')

load_dotenv()

with create_db_engine(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('PORT'),
    database=os.getenv('DATABASE')
) as eng:

    with eng.connect() as con:
        if database_exists(eng.url):
            print("EXISTE")
            print()
        else:
            print("NÃO EXISTE")

run_query(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('PORT'),
    database=os.getenv('DATABASE'),
    sql_file=os.path.join('helper', 'drop_tables.sql')
)

run_query(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('PORT'),
    database=os.getenv('DATABASE'),
    sql_file=os.path.join('helper', 'create_tables.sql')
)

insert_data(
    path=DATA_PATH,
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('PORT'),
    database=os.getenv('DATABASE'),
)