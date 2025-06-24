import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
dbname = os.getenv('DB_NAME')

# Monta a conexão dependendo se tem senha ou não
if password:
    db_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
else:
    db_uri = f"postgresql+psycopg2://{user}@{host}:{port}/{dbname}"

class Config:
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
