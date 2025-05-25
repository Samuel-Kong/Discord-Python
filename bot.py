import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f'The sum of {a} and {b} is {result}.')

@bot.command()
async def subtract(ctx, a: int, b: int):
    result = a - b
    await ctx.send(f'The difference between {a} and {b} is {result}.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Missing argument: {error.param.name}')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Invalid argument type provided.')
    else:
        await ctx.send('An error occurred while processing the command.')

@bot.command()
async def multiply(ctx, a: int, b: int):
    result = a * b
    await ctx.send(f'The product of {a} and {b} is {result}.')

@bot.command()
async def divide(ctx, a: int, b: int):
    if b == 0:
        await ctx.send('Cannot divide by zero.')
    else:
        result = a / b
        await ctx.send(f'The quotient of {a} and {b} is {result}.')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bot Information", description="This is a simple bot created with Discord.py.", color=0x00ff00)
    embed.add_field(name="Bot Name", value=bot.user.name, inline=True)
    embed.add_field(name="Bot ID", value=bot.user.id, inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="List of available commands:", color=0x00ff00)
    embed.add_field(name="!ping", value="Replies with Pong!", inline=False)
    embed.add_field(name="!hello", value="Greets the user.", inline=False)
    embed.add_field(name="!echo <message>", value="Repeats the message back to you.", inline=False)
    embed.add_field(name="!add <a> <b>", value="Adds two numbers.", inline=False)
    embed.add_field(name="!subtract <a> <b>", value="Subtracts b from a.", inline=False)
    embed.add_field(name="!multiply <a> <b>", value="Multiplies two numbers.", inline=False)
    embed.add_field(name="!divide <a> <b>", value="Divides a by b.", inline=False)
    embed.add_field(name="!info", value="Displays bot information.", inline=False)
    await ctx.send(embed=embed)



bot.run(BOT_TOKEN)