async def send_private(response, message, is_private):
    return (
        await message.author.send(response)
        if is_private
        else await message.channel.send(response)
    )
