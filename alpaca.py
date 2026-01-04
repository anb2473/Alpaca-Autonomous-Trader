import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv

# load environment vars from .env
# if you do not have a .env file replicate the example.env
load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET = os.getenv("ALPACA_SECRET")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL")

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET, ALPACA_BASE_URL, api_version='v2')

account = api.get_account()
