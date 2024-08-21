
import discord
import os 
from discord.ext import commands
from dotenv import load_dotenv
from botdata.client import Client



load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

if TOKEN is None:
    raise ValueError('Token not found in .env file')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)


