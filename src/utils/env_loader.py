import os
from dotenv import load_dotenv

def load_env():
    if os.getenv('AWS_LAMBDA_FUNCTION_NAME') is None:
        load_dotenv()