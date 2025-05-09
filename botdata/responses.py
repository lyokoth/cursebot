import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

curse_words = []
word_counts = {}

async def get_response(user_message: str) -> str:
    return 'Hello, I am ProfanityBot. I am here to help. How can I help?'


@bot.event
async def on_guild_join(guild):
    print(f'Joined server: {guild.name}')
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            welcome_message = ('Hello, I am ProfanityBot. I am here to help moderate your server to ensure that everyone is having a good and safe time.')
            await channel.send(welcome_message)
        break
    
@bot.command()
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
    await ctx.send(f'Curse words: {curse_words}')

@bot.command(name='count_swear')
async def count_swear(ctx):
    await ctx.send(f'Curse word counts: {word_counts}')

@bot.event
async def on_message(message):
    user_message = message.content.lower()
    author = message.author

    # Prevent the bot from replying to its own messages
    if author == bot.user:
        return

    # Check for curse words and count them
    words = user_message.split()
    found_curse_words = [word for word in words if word in curse_words]
    
    if found_curse_words:
        if author.name not in word_counts:
            word_counts[author.name] = 0
        word_counts[author.name] += len(found_curse_words)
        await message.channel.send(f'Warning {author.name}, please avoid using inappropriate language.')
        await message.delete()
    # Ensure commands are still processed
    await bot.process_commands(message)
    await message.channel.send(f'{author.name}, stop using inappropriate language.')

# Ensure you add the bot token here
bot.run('YOUR_BOT_TOKEN')