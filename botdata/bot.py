import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from collections import defaultdict

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
if TOKEN is None:
    raise ValueError('Token not found in .env file')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)  # Disable the default help command

curse_words = []  # Initialize the list for curse words
curse_word_count = defaultdict(int)  # Initialize a dictionary to count curse words

# Define a custom help command
class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()
    
    async def send_bot_help(self, mapping):
        channel = self.get_destination()
        response = (
            "Hello, I am ProfanityBot. I am here to help moderate your server to ensure that everyone is having a good and safe time. "
            "Here are some commands you can use:\n"
            "`$add_swear [word]`: Add a word to the list of curse words\n"
            "`$remove_swear [word]`: Remove a word from the list of curse words\n"
            "`$list_swear`: List all curse words\n"
            "`$count_swear`: Count the number of times each curse word has been used\n"
        )
        await channel.send(response)

bot.help_command = CustomHelpCommand()  # Set the custom help command

@bot.event 
async def on_ready():
    print(f'{bot.user} is now connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for curse words'))

    print("Registered commands:")
    for command in bot.commands:
        print(f" - {command.name}")

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            welcome_message = ("Hello, I am ProfanityBot. I am here to help moderate your server to ensure that everyone is having a good and safe time.")
            await channel.send(welcome_message)
        break

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    user_message = message.content.lower()

    detected_curse = False 
    for word in curse_words:
        if word in user_message:
            curse_word_count[word] += 1  # Increment the count for the curse word
            await message.delete()  # Delete the message with a curse word
            await message.channel.send(f"{message.author.mention}, please refrain from using offensive language.")
            detected_curse = True
            break  # No need to check further words once a match is found

    # Greeting Logic
    if not detected_curse:  # Only check for greetings if no curse word was detected
        greetings = ['hello', 'hi', 'hey', 'sup', 'yo']
        if any(greeting in user_message for greeting in greetings):
            response = f"Hello, {message.author.mention}, I am ProfanityBot. I am here to help."
            await message.channel.send(response)

    if isinstance(message.channel, discord.DMChannel) and message.content == "":
        await message.author.send("Hello, I am ProfanityBot. I am here to help. How can I help?")
    
    await bot.process_commands(message)  # Ensure other commands are processed

@bot.command(name='add_swear')
async def add_swear(ctx, word: str):
    if word in curse_words:
        await ctx.send(f'{word} is already in the list of curse words.')
        return
    curse_words.append(word)
    await ctx.send(f'{word} has been added to the list of curse words.')

@bot.command(name='remove_swear')
async def remove_swear(ctx, word: str):
    if word not in curse_words:
        await ctx.send(f'{word} is not in the list of curse words.')
        return
    curse_words.remove(word)
    await ctx.send(f'{word} has been removed from the list of curse words.')

@bot.command(name='list_swear')
async def list_swear(ctx):
    if not curse_words:
        await ctx.send('There are no curse words in the list.')
        return
    await ctx.send(f"Curse words: {', '.join(curse_words)}")

@bot.command(name='count_swear')
async def count_swear(ctx):
    if not curse_word_count:
        await ctx.send('No curse words have been used yet.')
        return
    counts = '\n'.join([f'{word}: {count}' for word, count in curse_word_count.items()])
    await ctx.send(f"Curses used:\n{counts}")

@bot.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use `$help` to see available commands.")
    else:
        # Print or log other errors
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    bot.run(TOKEN)
