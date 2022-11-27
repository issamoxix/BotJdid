import discord
from controllers import msg
import utils.utils as utils


def run_discord_bot():
    TOKEN = utils.get_token()

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

    
