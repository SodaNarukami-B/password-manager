import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State



load_dotenv() #загрузить
bot = Bot(token=os.getenv("BOT_TOKEN")) #токен
dp = Dispatcher() #мозг


