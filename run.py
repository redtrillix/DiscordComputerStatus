## Version: 1.0.0
## License: https://github.com/redtrillix/DiscordComputerStatus/raw/main/LICENSE
## Git Repository: https://github.com/redtrillix/DiscordComputerStatus
## Changelog: https://github.com/redtrillix/DiscordComputerStatus/blob/main/CHANGELOG.txt
## Owner: Zachary G (redtrillix)

import discord
from discord import Intents
import os
from datetime import datetime
import socket
import psutil

# Discord bot token
TOKEN = 'your_bot_token_here'

# Channel ID where you want to send the message
CHANNEL_ID = 'your_channel_id_here'

# Define the services that are up and running
services = ["Service1", "Service2", "Service3", "Service4", "Service5"]

# Get the current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get the hostname
hostname = socket.gethostname()

# Get the IP address
ip_address = socket.gethostbyname(hostname)

# Get CPU and memory usage
cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent

# Create the detailed message
MESSAGE = f"**System Notification:**\n\n"
MESSAGE += f"🔔 System turned on at {current_time}.\n"
MESSAGE += f"🖥️ Hostname: {hostname}\n"
MESSAGE += f"🌐 IP Address: {ip_address}\n"
MESSAGE += f"💻 CPU Usage: {cpu_usage}%\n"
MESSAGE += f"🧠 Memory Usage: {memory_usage}%\n\n"
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
