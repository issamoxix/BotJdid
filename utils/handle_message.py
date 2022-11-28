async def send_message_private(message_text, to):
    return await to.send(message_text)

async def send_message_to_channel(message_text,channel_id):
    return

async def send_message_curr_channel(message_text,message):
    await message.channel.send(message_text)

async def send_message_to_author(message_text,message):
    await message.author.send(message_text)

