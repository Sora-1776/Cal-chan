import math
import discord
from discord.ext import commands
import random
import time
from functools import reduce
import operator
def command_prefix(bot, message):
    if message.guild is None:
        return ''
    else:
        return [ ',', 'C ','c ' ]

intents = discord.Intents.all()     #can use all instead of default
bot = commands.Bot(command_prefix=command_prefix, description='[Bot name] helping...', case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx,*x: float):
    """Adds the given numbers together."""
    r=sum(x)
    await ctx.send(r)
@bot.command()
async def sub(ctx, left: float, right: float):
    """Subtracts two numbers."""
    await ctx.send(left-right)
@bot.command()
async def mul(ctx, *a: float):
    """Multiplies the given numbers together."""
    r=reduce(operator.mul,a)
    await ctx.send(r)

@bot.command()
async def div(ctx, left: float, right: float):
    """Divides two numbers."""
    await ctx.send(left/right)

@bot.command()
async def pl(ctx):
    """Gives the list of prefixes available"""
    await ctx.send('''The prefix list is :
``[ ',' - 'C ' - 'c ' ]``''')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, *content: str):
    """Repeats a message multiple times."""
    con = ' '.join(content)
    for i in range(times):
        await ctx.send(con)

@bot.group()
async def rd(ctx):
    """Delays for the given amount of time after each repeat."""
 
@rd.command(name='s')
async def repeatds(ctx,t: float, times: int, *content: str):
    """Delays for the given amount of seconds after each repeat."""
    con = ' '.join(content)
    for i in range(times):
        await ctx.send(con)
        time.sleep(t)
        
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.mention} joined in {0.joined_at}'.format(member))
    
@bot.command()
async def cool(ctx, member: discord.Member):
    """Says if the mentioned user is cool."""
    if ctx.invoked_subcommand is None:
            await ctx.send(random.choice(["{0.mention} is cool<:06:757169646003814433>", "{0.mention} is not cool<:03:757169544455520266>"]).format(member))
@bot.group()

async def iscool(ctx):
    """Says if a user is cool."""
    if ctx.invoked_subcommand is None:
        await ctx.send(random.choice([f"{ctx.author.mention} is cool<:06:757169646003814433>", f"{ctx.author.mention} is not cool<:03:757169544455520266>"]).format(ctx))
@iscool.command(name='bot')
async def bot_(ctx):
    """:Is the bot cool?"""
    await ctx.send('Yes, the bot is cool:star:.')

@bot.command()
async def clear(ctx, amount=5):
    """Clears the amount of messages specified. Default is 5."""
    await ctx.channel.purge(limit=amount)

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.id == bot.user.id:
        return 
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello **{0.author.name}**'.format(message))
    elif message.content.lower() == '''calc-b''' or message.content.lower() == '''calcb''':
        await message.channel.send('You rang?'.format(message))
    elif message.author.id == 447523127996710912 and message.content.lower() == 'hey':
        await message.channel.send('he-...hey<:01:757169328213721118>...')
    
    await bot.process_commands(message)
    
bot.run('[Bot Token]')          #remove the []
