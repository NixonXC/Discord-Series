import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")

@bot.event
async def on_ready():
  print("I am Alive!")
  
bot.run("TOKEN")
