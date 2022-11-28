from utils import handle_message


async def msg_process(message, client, brain):
    username = message.author
    if client.user == username:
        return
    name = username.name
    user_message = str(message.content)
    if "!" in user_message:
        if user_message[0] == "!":
            msg_splited = user_message[1:].split()
            command = msg_splited[0]
            if command == "hello":
                response = f"Hello {name} !"
                return await handle_message.send_message_curr_channel(response, message)
            if command == "gol":
                mention = brain.members.get(brain.get_id_from_mention(msg_splited[1]))
                text_response = " ".join(msg_splited[2:])
                return await handle_message.send_message_private(text_response, mention)
            if command == "say":
                response = " ".join(msg_splited[1:])
                return await handle_message.send_message_curr_channel(response, message)

    if "bot" in user_message:
        response = f"nta li {user_message.replace('bot','')}"
        return await handle_message.send_message_to_author(response, message)
