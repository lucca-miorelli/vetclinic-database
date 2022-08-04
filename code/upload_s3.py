import boto3
import awswrangler as wr
from dotenv import load_dotenv
import os
import pandas as pd

DATA_PATH = os.path.join('data', 'vetclinic_procedures.parquet')

load_dotenv()

session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

wr.s3.to_parquet(
    df=pd.read_parquet(DATA_PATH),
    path='s3://poatek-de-mentorship/session_6/vetclinic_procedures.parquet',
    dataset=False,
    boto3_session=session
)
