import discord
import os
import random
import selenium_app

from discord.ext import commands;
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

client = discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to the server!!')

@bot.command(name="talk", help="responds with a random quote online!")
async def on_talk(ctx):

    texts = [
        "I like baseball!",
        "Your life is a lie!",
        "My teacher loves playing basketball!",
        "You are lonely as fuck!",
        "My grandma can do better than you!",
        "Shit will get real pretty soon",
        "I hate my life",
        "Kill me right now."
    ]

    response = random.choice(texts)
    await ctx.send(response)

@bot.command(name="instaSpam", help='spams messages to anyuser on instagram!')
async def automateMSG(ctx, username: str, count: int):
    await selenium_app.main(username=username, count=count)

@bot.command(name='dice', help='help simulate rolling dice')
async def on_call_dice(mcontext, num_dics: int, num_sides: int):

    options = [
        str(random.choice(range(1, num_sides + 1)))
        for _ in range(num_dics)
    ]

    await mcontext.send(('\n -').join(options))

bot.run(token)