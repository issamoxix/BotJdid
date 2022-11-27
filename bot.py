import discord
import responses
from utils.privelage import send_private
from message_process import msg
import json

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await send_private(response, message, is_private)

    except Exception as e:
        print(e)


def run_discord_bot():
    with open('secrets.json','r') as file:
        try:
            TOKEN = json.loads(file.read())["TOKEN"]
        except:
            raise Exception("TOKEN doesn't exists on the secrets.json file !")

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running ! ")

    @client.event
    async def on_message(message):
        await msg.msg_process(message, client)
    client.run(token=TOKEN)

    
