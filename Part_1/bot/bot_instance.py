import os
from aiogram import Bot, types

from config import TOKEN_API
# Use the commented code below if you store the token api in .env
# from dotenv import load_dotenv
# load_dotenv()

bot = Bot(
    token=TOKEN_API,
    parse_mode='HTML'
)