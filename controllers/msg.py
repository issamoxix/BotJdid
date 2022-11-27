from utils import privelage
from discord import VoiceClient


async def msg_process(message, client):
    username = message.author
    if client.user == username:
        return

    # channel = client.get_channel(1046447744086200404)
    # voiceClient = VoiceClient(client=client, channel=channel)

    name = username.name
    user_message = str(message.content)
    is_private = False
    if user_message[0] == "!":
        msg = user_message[1:]
        if msg == "hello":
            response = f"Hello {name} !"
            return await privelage.send_private(response, message, is_private)

        # if msg == "aji":
        #     await voiceClient.connect(timeout=15, reconnect=True)
        # if msg == "ser":
        #     await voiceClient.disconnect()

    if "bot" in user_message: 
        response = f"nta li {user_message.replace('bot','')}"
        is_private = True
        return await privelage.send_private(response, message, is_private)
