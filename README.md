# Computer Status Discord Bot

This Python script sends a notification message to a Discord channel when the computer is turned on. The message includes system information such as the current time, hostname, public IP address, CPU usage, memory usage, and a list of specified running services.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages: `discord.py`, `psutil`, `requests`, `python-dotenv`.
- A Discord bot token. You can create a new bot and get its token from the Discord Developer Portal.

## Installation

1. Clone this repository to your local machine or download the ZIP file.
2. Navigate to the project directory.

3. Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

4. Edit the `.env` file in the project directory and add your Discord bot token and channel ID in the following format:

```
TOKEN=your_bot_token_here
CHANNEL_ID=your_channel_id_here
```

## Usage

1. Run the script using the following command:

```bash
python run.py
```

2. The script will send a notification message to the specified Discord channel with system information when the computer runs this script.

## Customization

- You can customize the list of running services by modifying the `services` list in the script.
- Additional system information or features can be added as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
