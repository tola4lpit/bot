import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore bot messages

    if message.content.lower() == "help911":
        await message.channel.send("Sending help to this bitch")

    await bot.process_commands(message)  # Allow commands to work

# Run the bot
bot.run(TOKEN)
