import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get('client_id', None)
CLIENT_SECRET = os.environ.get('client_secret', None)