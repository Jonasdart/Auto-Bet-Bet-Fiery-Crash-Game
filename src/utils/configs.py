import os
from dotenv import load_dotenv

load_dotenv(".env")

EMAIL = os.getenv("email").strip()
PASSWORD = os.getenv("password").strip()
BET_PERCENT = int(os.getenv("BET_PERCENT", "20"))
MAX_BET = int(os.getenv("MAX_BET", "18"))
MIN_PURSE = float(os.getenv("MIN_PURSE", "10"))
MULTI_ODD = float(os.getenv("ODD", "1.4"))
MULTI_LOSE = float(os.getenv("MULTI_LOSE", "1"))
SAQUE = int(os.getenv("SAQUE", "100"))
