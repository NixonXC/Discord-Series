import discord

slash = discord.Bot()

@slash.slash_command()
async def ping(ctx):
  await ctx.send("Pong!")

@slash.event
async def on_ready():
  print("I am Alive!")
  
slash.run("TOKEN")
