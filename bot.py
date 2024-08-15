import discord
from discord.ext import commands
#hola
intents = discord.Intents.default()
intents.message_content = True
token = ""
bot = commands.Bot(command_prefix= "/", intents=intents)

@bot.event
async def on_ready():
    print(f"hola, soy {bot.user}")

@bot.command(name="hi")
async def hello(ctx, nombre):
    await ctx.send(f"hola:, {bot.user} un gusto {nombre}")


bot.run (token) 
