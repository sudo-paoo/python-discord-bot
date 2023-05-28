import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime
from datetime import datetime
import time
import pytz
import requests
import json

# LOAD DOTENV

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
QR_URL = os.getenv('QR_URL')
NASA_API = os.getenv('NASA_API')
NASA_URL = os.getenv('NASA_URL')
U_FACTS = os.getenv('U_FACTS')


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)
command_l = ['apod', 'ufacts', 'qr']
@bot.event
@commands.has_permissions(administrator=True)

# BOT ON READY

async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="onlne users"))

#  PING COMMAND

@bot.command()
async def ping(ctx):
    global times
    global tz
    try:
        await ctx.send(f'[ |{datetime.now(tz).strftime("%H:%M:%S")} ] Status > Online | Startup > {round(time.time() - times, 1)}s')
    except:
        await ctx.send("There was an error on the server. Please try again")

# STATUS

@bot.command()
async def status(ctx):
    await ctx.send(f'Online! Latency: {round(bot.latency, 3)} ms')

# LIST OF COMMANDS

@bot.command()
async def list(ctx):
    try:
        embed = discord.Embed(
            color=discord.Colour.dark_teal(),
            title=f"""
            Hey  there {ctx.message.author}!\n\nI am online, therefore I can assist you on you need! Here are my current available commands as of now.""",
            description=f"""Commands:
            ?ping
            📖Check if my alive or not
            ?status
            📖Provide the latency of the bot
            ?list
            📖Provide an overview of my commands
            ?apod
            📖Provides the Astronomy Picture of the Day
            ?generateqr
            📖Generates a qr code from the given text
            ?ufacts
            📖Send useless facts
            ?qoute
            📖Provides a random qoute with author"""
        )

        await ctx.send(embed=embed)
    except:
        await ctx.send("There was an error on the server. Please try again")

# NASA ASTRONOMY PICTURE OF THE DAY

@bot.command()
async def apod(ctx):
    await ctx.send("Send a date to find the NASA image of the day. YYYY-MM-DD format.")
    try:
        def check(author):
            def inner_check(message):
                return message.author == author and message.content
            return inner_check

        msg = await bot.wait_for("message", check=check(ctx.author))
        date = msg.content
        params = {
            'api_key': NASA_API,
            'hd': 'True',
            'date': date
            }
        resp = requests.get(NASA_URL + NASA_API, params=params)
        respData = json.loads(resp.text)
        date = respData['date']
        title = respData['title']
        explanation = respData['explanation']
        embed = discord.Embed(
            url=respData['hdurl'],
            color = discord.Colour.dark_teal(),
            title=title,
            description=f"Date:{date}\n\nDescription:\n\n{explanation}",
        )

        embed.set_footer(text="Information provided is from NASA")
        await ctx.send(embed=embed)
    except:
        date = msg.content
        params = {
            'api_key': NASA_API,
            'hd': 'True',
            'date': date
            }
        resp = requests.get(NASA_URL + NASA_API, params=params)
        respData = json.loads(resp.text)
        date = respData['date']
        title = respData['title']
        explanation = respData['explanation']
        embed = discord.Embed(
            url=respData['url'],
            color = discord.Colour.dark_teal(),
            title=title,
            description=f"Date:{date}\n\nDescription:\n\n{explanation}",
        )

        embed.set_footer(text="Information provided is from NASA")
        await ctx.send(embed=embed)

# USELESS FACTS

@bot.command()
async def ufacts(ctx):
    try:
        uf = requests.get(U_FACTS)
        data = json.loads(uf.text)
        await ctx.send(f"Useless Fact:\n\n {data['text']}")
    except:
        await ctx.send('Sorry there was an error finding a  useless fact. Please try again.')

# GENERATE QR

@bot.command()
async def generateqr(ctx):
    await ctx.send("Please provide the text you want to generate a qr code.")
    try:
        def check(author):
            def inner_check(message):
                return message.author == author and message.content
            return inner_check

        msg = await bot.wait_for("message", check=check(ctx.author))

        qr_code = QR_URL + msg.content.replace(' ','%20')
        await ctx.send(qr_code)
    except:
        await ctx.send("Error getting data from the server")

# QOUTES

@bot.command()
async def qoute(ctx):
    try:
        r = requests.get('https://zenquotes.io/api/random')
        j = json.loads(r.text)

        await ctx.send(f"{j[0]['q']}\n\nAuthor: {j[0]['a']}")
    except:
        await ctx.send("Error getting data from the server")

if __name__ == '__main__':
    times = time.time()
    tz = pytz.timezone('Asia/Manila')
    bot.run(BOT_TOKEN)