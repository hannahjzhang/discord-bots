import discord
import hello_world_key

TOKEN = hello_world_key.KEY
# create discord client
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user.name} has connected to Discord')

# respond to certain messages
@client.event
async def on_message(message):
  # check if message is from ourselves to avoid infinite loop
  if message.author == client.user:
    return
  if message.content == ('hello'):
    await message.channel.send('world')
    await message.add_reaction('🌝')
  if message.content == ('world'):
    await message.channel.send('oh hello')
    await message.add_reaction('🌚')

# respond to certain reactions
@client.event
async def on_reaction_add(reaction, user):
  react = str(reaction)
  if react == "👋":
    await channel.send('hello to you toooooo')
  if react == '🌎':
    await channel.send('world hello world')

# to run the bot
client.run(TOKEN)
