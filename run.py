## Version: 2.1.0
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
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord bot token
TOKEN = os.getenv('TOKEN')

# Channel ID where you want to send the message
CHANNEL_ID = os.getenv('CHANNEL_ID')

# Retrieve services from .env and split them into a list
SERVICES = os.getenv('SERVICES').split(',')

# Get the current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get the hostname
hostname = socket.gethostname()

# Get the public IP address
try:
    public_ip = requests.get('https://httpbin.org/ip').json()['origin']
except Exception as e:
    public_ip = "Unavailable"

# Get CPU and memory usage
cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent

# Create the detailed message
MESSAGE = f"**System Notification:**\n\n"
MESSAGE += f"🔔 System turned on at {current_time}.\n"
MESSAGE += f"🖥️ Hostname: {hostname}\n"
MESSAGE += f"🌐 Public IP Address: {public_ip}\n"
MESSAGE += f"💻 CPU Usage: {cpu_usage}%\n"
MESSAGE += f"🧠 Memory Usage: {memory_usage}%\n\n"
MESSAGE += "**Services Running:**\n\n"
MESSAGE += "```"
MESSAGE += f"{'Service':<20}{'Status':<10}\n"
MESSAGE += "-" * 30 + "\n"
for service in SERVICES:
    MESSAGE += f"{service:<20}{'Running':<10}\n"
MESSAGE += "```"

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
