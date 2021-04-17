import discord
import os
from keep_alive import keep_alive
from db_queries import update_search_history, get_search_results

# Intializing bot
client = discord.Client()


# To Check if server is ready
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  # if message.author == client.user:
  #   return 
  if message.content.startswith('hi'):
    await message.channel.send("Hey")
  elif message.content.startswith('!google'):
    searched_words = message.content.split()[1:]
    user = message.author
    result = update_search_history(' '.join(searched_words), user)
    await message.channel.send(result)
  elif message.content.startswith('!recent'):
    searched_words = message.content.split()[1:]
    result = get_search_results(' '.join(searched_words))
    await message.channel.send(result)

# To Keep server running
keep_alive()

client.run(os.getenv('TOKEN'))
