from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from contextlib import contextmanager
import pandas as pd
import os

@contextmanager
def create_db_engine(user, password, host, port, database):
    try:
        engine = create_engine(
            f"postgresql://{user}:{password}@{host}:{port}/{database}",
            echo=False
        )
        yield engine
    except:
        print('Database does not connect.')
    finally:
        engine.dispose()

def run_query(user, password, host, port, database, sql_file):
    
    with open(sql_file, 'r') as query:
        query_text = query.read()
        with create_db_engine(user=user, password=password, host=host, port=port, database=database) as eng:
            with eng.connect() as con:            
                # EXECUTE QUERY
                try:
                    for command in query_text.split(';'):
                        print('='* 50)
                        print(command)
                        con.execute(statement=command)
                        print("The query above was run.")
                        print('-'* 50, '\n')
                except:
                    print("Query did not run")
                
            print("Connection to DB closed.")
        print("Engine of DB closed.")
    print("SQL file closed.")

def read_data(path):
    dataframe = pd.read_parquet(path)
    dataframe.columns = dataframe.columns.str.lower()
    return dataframe

def process_data(dataframe):
    data_splitted = split_data(dataframe)
    owners, pets, procedures_history, procedures_details = transform_data(data_splitted)
    return [owners, pets, procedures_history, procedures_details]

def split_data(dataframe):

    print(f'Splitting owners')
    owners = dataframe[[
        'ownerid',
        'ownername',
        'ownersurname',
        'streetaddress',
        'city',
        'state',
        'statefull',
        'zipcode'
    ]]
    print(f'Splitting pets')

    pets = dataframe[[
        'petid',
        'petname',
        'petkind',
        'petgender',
        'petage',
        'ownerid'
    ]]

    procedures_history = dataframe[[
        'petid',
        'date',
        'proceduretype',
        'proceduresubcode'
    ]]

    procedures_details = dataframe[[
        'proceduretype',
        'proceduresubcode',
        'description',
        'price'
    ]]

    return [owners, pets, procedures_history, procedures_details]

def transform_data(tables_list):
   
    owners, pets, procedures_history, procedures_details = tables_list

    for df in [owners, pets, procedures_details]:
        df.drop_duplicates(
            keep='first',
            inplace=True
        )

    owners.drop_duplicates(
        subset=['ownerid'],
        keep='last',
        inplace=True
    )
    
    owners['ownerid'] = owners['ownerid'].astype('object')
    owners['zipcode'] = owners['zipcode'].astype('object')
    pets['ownerid'] = pets['ownerid'].astype('object')
    procedures_history.insert(0, 'procedureid', range(1, 1 + len(procedures_history)))
    procedures_history['procedureid'] = procedures_history['procedureid'].astype('object')
    procedures_history['proceduresubcode'] = procedures_history['proceduresubcode'].astype('object')
    procedures_details['proceduresubcode'] = procedures_details['proceduresubcode'].astype('object')

    return [owners, pets, procedures_history, procedures_details]


def insert_data(path, user, password, host, port, database):

    tables_list = process_data(
        read_data(path)
    )

    for df in tables_list:
        print(df.shape)
        print(df.dtypes)
        print(df.columns)
        print(type(df))
        print('\n')
    
    owners, pets, procedures_history, procedures_details = tables_list

    with create_db_engine(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
    ) as eng:     

        try:
            owners.to_sql(
                'owners',
                con=eng,
                if_exists='append',
                index=False,
                schema='public'
            )
            pets.to_sql(
                'pets',
                con=eng,
                if_exists='append',
                index=False,
                schema='public'
            )
            
            print(procedures_details)

            procedures_details.to_sql(
                'procedures_details',
                con=eng,
                if_exists='append',
                index=False,
                schema='public'
            )

            procedures_history.to_sql(
                'procedures_history',
                con=eng,
                if_exists='append',
                index=False,
                schema='public'
            )

        except Exception as e:
            print(e)
