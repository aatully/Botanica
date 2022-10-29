import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    content = message.content
    user = message.author
    channel = message.channel

    if user == client.user:
        return

    print("Received a message:", content)

    if content.strip() == "hello":
        await channel.send("Hi!")

    if content.strip() == "die":
        await channel.send("Bye... :(")
        client.close()

client.run(os.getenv('TOKEN'))