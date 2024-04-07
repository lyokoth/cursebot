import discord 


class Client:
    async def on_message(self, message):
        if message.author == self.user:
            return 


        if message.content.startsWith('$hello'):
            await message.channel.send('Welcome back!')

        elif message.content.startsWith('$how are you?'):
            await message.channel.send('I am a bot, so I do not have feelings, but thank you for asking!')
    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for curse words'))
        