import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the current directory
load_dotenv()

def read_env_variable(key, default=None):
    """
    Read an environment variable from the .env file.

    Args:
        key (str): The name of the environment variable to read.
        default (str, optional): A default value to return if the variable is not found.

    Returns:
        str: The value of the environment variable or the default value if not found.
    """
    return os.getenv(key, default)
