import dice_bot_key
import discord
from random import randint

TOKEN = dice_bot_key.KEY
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  # be on the lookout for a call to dice bot
  if message.content == ('roll') or ('dice'):
    randNum = randint(1, 6)
    await message.add_reaction('👍')
    await message.channel.send(randNum)

client.run(TOKEN)
