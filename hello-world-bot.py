import discord
import key

#create discord client
client = discord.Client()

@client.event
async def on_message(message):
  #check if message is from ourselves to avoid infinite loop
  if message.author == client.user:
    return

  if message.content == ('!hello'):
    await message.channel.send('world')
    await message.add_reaction('🌎')

  if message.content == ('!world'):
    await message.channel.send('oh hello')
    await message.add_reaction('👋')

# to run the bot
client.run(key.KEY)