import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# load token from safe file
load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')

# Load intents
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Message functions
async def send_message(message : Message, user_message : str, is_private : bool = False) -> None:
    # Checks if intents are met
    if not user_message:
        print('Message empty because intents not met')
        return
    
    # Checks if users message contains command prefix, and parses it
    has_prefix = user_message[0] == '%'
    if has_prefix:
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(embed=response)
    # Catches and prints errors
    except Exception as e:
        print(e)

# Bot startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling incoming messages
@client.event
async def on_message(message : Message) -> None:
    if message.author == client.user:
        return
    
    username : str = str(message.author)
    user_message : str = message.content
    channel : str = str(message.channel)

    # Shows message in console
    print(f'[{channel}] {username}: {user_message}')
    await send_message(message, user_message)

# Runs bot client
def main() -> None:
    client.run(token=bot_token)

if __name__ == '__main__':
    main()