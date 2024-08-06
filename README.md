
# General Purpose Valorant Bot

This is a Discord bot built using the Discord.py library. The bot fetches and processes data from an API to provide information about Valorant players.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Valorant Discord Bot is a general-purpose bot for Discord designed to provide Valorant-related information and functionalities. This bot utilizes the Valorant API to fetch real-time game data, match statistics, and more. It is built using Python and the `discord.py` library to interface with Discord's API.

### APIs Used

-<a href="https://github.com/Henrik-3/unofficial-valorant-api">**unofficial valorant api**</a> by <a href="https://github.com/Henrik-3">__Henrik 3__</a>: Provides data related to Valorant matches, player statistics, and other game information.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12.2 or higher is installed on your machine.
- [pip](https://pip.pypa.io/en/stable/installation/) is installed for package management.
- A Discord account and a server where you can add the bot.
- A registered Discord application with a bot token. You can register a bot at the [Discord Developer Portal](https://discord.com/developers/applications).

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/discord-bot.git
   cd discord-bot
   ```

2. **Create a Virtual Environment**

   Create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   Install the necessary Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` File**

   In the root directory of the project, create a `.env` file to store your sensitive information like the Discord bot token and any API keys.

   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   API_KEY=your_api_key_here
   ```

2. **Configure Environment Variables**

   Ensure your `.env` file is correctly formatted and saved in the project’s root directory. The `.env` file should not be included in version control, as it contains sensitive information. Make sure your `.gitignore` file includes:

   ```
   .env
   ```

## Running the Bot

1. **Activate the Virtual Environment**

   Ensure the virtual environment is activated:

   ```bash
   # Windows
   .\venv\Scripts\activate

   # macOS and Linux
   source venv/bin/activate
   ```

2. **Run the Bot**

   Start the Discord bot using:

   ```bash
   python discord_bot.py
   ```

   The bot should connect to Discord and begin running, displaying a message in the console indicating it is online.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.