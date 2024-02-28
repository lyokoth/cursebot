import discord 

from discord.ext import commands
from dotenv import load_dotenv

client_id = load_dotenv('CLIENT_ID')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event 
async def on_server_join(guild):
    for channel in guild.text_channels:
        welcome_message = (f'Hello, I am ProfanityBot. I am here to help moderate your server to ensure that everyone is having a good and safe time.')
        await channel.send(welcome_message)


## when user is kicked 
@bot.event
async def on_member_remove(member):
    await member.send(f'Goodbye {member.name}, you have been kicked from the server. If you believe this was a mistake, please contact the server owner.')


## run the bot 
def run_bot():
    TOKEN = load_dotenv('TOKEN')
    bot.run(TOKEN)


# Path: app.py