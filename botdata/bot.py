import discord 
from discord.ext import commands
from dotenv import load_dotenv
import os
import responses 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event 
async def on_slap(ctx, member: discord.Member, *, reason="no reason"):
    await ctx.send(f"{ctx.author.name} slapped {member.name} for {reason}")


async def send_msg(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = load_dotenv(TOKEN)
    client = discord.Client()

    @client.event
    async def on_ready():  
        print(f'{client.user} has connected to Discord!')


    client.run(TOKEN)