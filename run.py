## Version: 0.2.0
## Git Repository: https://github.com/redtrillix/DiscordComputerStatus
## License: https://github.com/redtrillix/DiscordComputerStatus/raw/main/LICENSE
## Owner: Zachary G (redtrillix)

import discord
from discord import Intents
import os

# Discord bot token
TOKEN = 'your_bot_token_here'

# Channel ID where you want to send the message
CHANNEL_ID = 'your_channel_id_here'

# Define the services that are up and running
services = ["Service1", "Service2", "Service3"]

# Create the detailed message
MESSAGE = "Computer is turned on! Services that are up and running:\n\n"
for service in services:
    MESSAGE += f"- {service}\n"

# Define the intents
intents = Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True  # Enable receiving message events

# Create a Discord client with intents
client = discord.Client(intents=intents)

# Event called when the bot is ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # Fetch the channel
    channel = client.get_channel(int(CHANNEL_ID))
    if channel:
        # Send the message
        await channel.send(MESSAGE)
    else:
        print("Channel not found.")

# Run the bot
client.run(TOKEN)
