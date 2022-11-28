import discord
from controllers import msg
import utils.utils as utils
from models.brain import Brain


def run_discord_bot():
    TOKEN = utils.get_token()

    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True
    intents.members = True
    client = discord.Client(intents=intents)

    brain = Brain(client)

    @client.event
    async def on_ready():
        brain.set_brain()
        print(f"{client.user} is running ! ")

    @client.event
    async def on_message(message):
        await msg.msg_process(message, client, brain)

    @client.event
    async def on_member_join(member):
        print(member.name, "dkhal l sever")

    client.run(token=TOKEN)
