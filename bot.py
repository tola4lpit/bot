import discord
from discord.ext import commands
import yt_dlp

intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages

bot = commands.Bot(command_prefix="$", intents=intents)  # Prefix changed to $

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def join(ctx):
    """Make the bot join the voice channel."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You need to be in a voice channel first!")

@bot.command()
async def leave(ctx):
    """Make the bot leave the voice channel."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel!")

@bot.command()
async def play(ctx, url):
    """Play a YouTube video audio."""
    if not ctx.voice_client:
        await ctx.invoke(join)  # Make the bot join first if not in VC

    voice_client = ctx.voice_client
    ydl_opts = {'format': 'bestaudio'}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']
    
    ffmpeg_options = {'options': '-vn'}
    voice_client.play(discord.FFmpegPCMAudio(audio_url, **ffmpeg_options))

bot.run("MTM1MjMxODY4OTQxMTU5NjM0OQ.GuZ_cR.EzPuZ8a3ElJEQxm1PZSqbuQotQswPtA4Gg1Oco")
