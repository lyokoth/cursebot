## ProfanityBot (previously known as cussbot)


A discord bot that can censor curse words so everyone can have a good time!


# ProfanityBot Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Setup Instructions](#setup-instructions)
3. [Bot Commands](#bot-commands)
4. [Events Handled by the Bot](#events-handled-by-the-bot)
5. [Error Handling](#error-handling)
6. [Customization and Contribution](#customization-and-contribution)
7. [License](#license)

### Introduction

**ProfanityBot** is a Discord bot designed to help moderate your server by detecting and removing profanity from messages. It offers various commands to manage the list of forbidden words and provides statistics on the usage of these words.

### Setup Instructions

To set up ProfanityBot on your Discord server, follow these steps:

1. **Clone the repository**: Download or clone the bot's source code to your local machine.

   ```bash
   git clone <repository-url>
   cd ProfanityBot


2. **Install Dependencies:**: Make sure you have Python installed (v3.8 or higher) and install required libraries using pip:

    ```bash
    pip install discord.py python-dotenv


3.  Create a Discord Bot: Go to the Discord Developer Portal, create a new application, and add a bot to it. Copy the bot token.

4. Setup Environment Variables: Create a .env file in the root directory of the project and add your bot token:
    ```bash 
     BOT_TOKEN=your_discord_bot_token


5. Run the bot using this Python script.

    ```bash
     python bot.py


    
Currently, the bot has several commands to manage and moderate your server. More will be added in the future:

 - $add_swear[word]: Adds a word to the list.
 - $remove_swear[word]: Removes a word from the list
 - $list_swear: Lists all curse words being tracked.



 # Events handled by bot.

 - on_ready: Triggered when the bot successfully connects to Discord. It updates the bot's status to show that it is monitoring swear words.

- on_guild_join: Triggered when the bot joins a new server (guild). It sends a welcome message to the server's general channel.

- on_message: Listens to all messages sent in the server. If a message contains a swear word, it deletes the message and warns the user. It also responds to greetings such as "hello," "hi," "hey," etc. 


# Future Features 
 - Add ability to kick a user when they have used a swear or a filtered word more than x amount of times (progressive warning)





