import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

curse_words = ['shit', 'fuck']
word_counts = {}

## for server messages 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    
    if message.content.lower() in curse_words:
        await message.channel.send(f'{message.author.mention}, you have been warned for using a curse word. ')
        if message.author.id in word_counts:
            word_counts[message.author.id] += 1
        else:
            word_counts[message.author.id] = 1
        if word_counts[message.author.id] == 3:
            await message.channel.send(f'{message.author.mention} has been kicked for using a curse word. ')
            await message.author.kick(reason='Using a curse word')
            del word_counts[message.author.id]
    await bot.process_commands(message)


## for DMs

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello, thanks for using the ProfanityBot!'
    
    if p_message == 'how are you?':
        return 'I am a bot, so I do not have feelings, but thank you for asking!'
    
    if p_message == 'can i swear?':
        return 'Please do not swear.'
    

    if p_message == '$help':
        return 'This is a message you can modify'
    

    return 'I am a bot, so I do not understand that message. More commands will be updated soon I believe.'