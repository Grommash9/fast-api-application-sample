from dotenv import load_dotenv

load_dotenv()
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MYSQL = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'db': os.getenv('MYSQL_DB_NAME'),
    'port': int(os.getenv('MYSQL_PORT'))
}

api_port = int(os.getenv('api_port'))


