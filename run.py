## Version: 0.3.1
## License: https://github.com/redtrillix/DiscordComputerStatus/raw/main/LICENSE
## Git Repository: https://github.com/redtrillix/DiscordComputerStatus
## Changelog: https://github.com/redtrillix/DiscordComputerStatus/blob/main/CHANGELOG.txt
## Owner: Zachary G (redtrillix)

import discord
from discord import Intents
import os
from datetime import datetime

# Discord bot token
TOKEN = 'your_bot_token_here'

# Channel ID where you want to send the message
CHANNEL_ID = 'your_channel_id_here'

# Define the services that are up and running
services = ["Service1", "Service2", "Service3"]

# Get the current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create the detailed message
MESSAGE = f"**System Notification:**\n\n"
MESSAGE += f"🔔 System turned on at {current_time}.\n"
MESSAGE += "**Services Running:**\n\n"
MESSAGE += "\n".join([f"- {service}" for service in services])

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
