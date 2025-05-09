import discord 
import os
from dotenv import load_dotenv


class Client(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return 


        if message.content.startswith('$hello'):
            await message.channel.send('Welcome back!')

    
    async def on_ready(self):
        print(f'{self.user} is now connected to Discord!')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for swear words'))


client = Client(intents=discord.Intents.default())
client.run('BOT_TOKEN')

