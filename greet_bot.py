import discord
import greet_bot_key

TOKEN = greet_bot_key.KEY
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user.name} has connected to Discord')

@client.event
async def on_member_join(member):
  # send personalized welcome dm
  await member.create_dm()
  await member.dm_channel.send(f'Hi ' + member.name + " , I'm so excited you're here!")
  # send public welcome message
  await client.send_message(discord.Object(id='CHANNELID'), 'Welcome ' + member.name + ' !')

@client.event
async def on_member_remove(member):
  # public leaving message
  await client.send_message(discord.Object(id='CHANNELID'), member.mention + ' just left. Hope to see you later!')

client.run(TOKEN)
