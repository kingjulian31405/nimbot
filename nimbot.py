import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo")
@bot.command(name='flip_coin')
async def flip_coin(ctx):
    import random
    await ctx.send(randomchoice(['Heads', 'Tails']))
@bot.command(name='avg')
async def avg(ctx,*args: float):
    await ctx.send(sum(args)/ len(args))
bot.run(token)
@bot.command(name='roll_dice')
async def roll_dice(ctx, x):
    from random import randint
    await ctx.send(randint(1,x))

