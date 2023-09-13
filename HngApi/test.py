import os
from dotenv import load_dotenv
load_dotenv()
import os

# Get the ALLOWED_HOSTS value from the .env file and split it into a list
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
print(ALLOWED_HOSTS)