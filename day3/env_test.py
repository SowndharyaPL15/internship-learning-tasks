
import os
from pathlib import Path
from dotenv import load_dotenv

# Load the .env file from the day3 folder
env_file = Path(__file__).with_name(".env")
load_dotenv(env_file)

api_key = os.getenv("API_KEY")
app_env = os.getenv("APP_ENV", "development")

print("API key loaded:", bool(api_key))
print("Application environment:", app_env)
