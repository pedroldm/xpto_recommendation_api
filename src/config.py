import os

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
SALES_BIAS = os.getenv("SALES_BIAS")
PRICE_BIAS = os.getenv("PRICE_BIAS")
STORE_SALES_BIAS = os.getenv("STORE_SALES_BIAS")

def get_database_path() -> str:
    return DB_PATH

def get_sales_bias() -> float:
    return SALES_BIAS

def get_price_bias() -> float:
    return PRICE_BIAS

def get_store_sales_bias() -> float:
    return STORE_SALES_BIAS