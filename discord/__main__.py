import discord

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  if message.author != client.user:
    msg = message.author.mention + " Hi."
    await client.send_message(message.channel, msg)

client.run("NzMxMTYzNzE4ODAwNTA2ODkw.XwiMIA.xU5zDI0-AS0ZyvPoH2TToNy_6MI")
