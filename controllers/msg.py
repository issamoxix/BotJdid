from utils import privelage
from discord import VoiceClient, FFmpegPCMAudio, VoiceChannel, Guild


async def msg_process(message, client):
    username = message.author
    if client.user == username:
        return

    url = "https://rr5---sn-i5h7lnls.googlevideo.com/videoplayback?expire=1669602716&ei=PMmDY9JQyduAB5WLmpAH&ip=2a00%3A1f%3A93c0%3A7101%3A67%3A3e64%3A5ede%3Af14f&id=o-AIxCz6h5kiYVJvxZfCRkbcdBP_BxAZ4PdsPdVFCKYT4r&itag=249&source=youtube&requiressl=yes&mh=oA&mm=31%2C26&mn=sn-i5h7lnls%2Csn-4g5lznl6&ms=au%2Conr&mv=m&mvi=5&pl=42&gcr=de&initcwndbps=1051250&vprv=1&mime=audio%2Fwebm&ns=uIF5OZrcIcSQxf2afqzoF1cJ&gir=yes&clen=2916440&dur=432.821&lmt=1584185855706374&mt=1669580741&fvip=4&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5431432&n=xvG7kR5rSC98ttj&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhALwRY0BTsJxuypeB4aiXHbPGMpy3wdKUXhQLg2TrV3FQAiBnnpHqRrYu7zbdUs8OFpDCvsAbInbr-THRctmm1hRAag%3D%3D&sig=AOq0QJ8wRQIgMbLRn4Ka1XFGLHUtcuAawva5mDsLCOVupkPCPJs2UEoCIQCS80jJKGmdxrIgjQJ0S1WVKiIcLYn9M9yMEZqfC5zRHw=="
    FFMPEG_OPTIONS = {
        "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        "options": "-vn",
    }
    name = username.name
    user_message = str(message.content)
    is_private = False
    if "!" in user_message:
        if user_message[0] == "!":
            msg = user_message[1:]
            msg_splited = msg.split()
            if msg == "hello":
                response = f"Hello {name} !"
                return await privelage.send_private(response, message, is_private)

            if msg_splited[0] == "aji":
                channel_name = msg_splited[1].lower()
                for i in client.get_all_channels():
                        try:
                            finished = False
                            # channel = client.get_channel(1046447744086200404)
                            if str(i).lower() == channel_name:
                                # try:
                                g = Guild(name="Issam's server",id="1046447743410913400")
                                voicechannel = VoiceChannel(guild=g)
                                voicechannel.name = i.name
                                voicechannel._get_channel(i)

                                voicechannel.connect(reconnect=True, timeout=15)
                                voiceClient = VoiceClient(client=client, channel=i)
                                # voiceClient.connect(reconnect=True,timeout=15)
                                voiceClient.play(
                                    source=FFmpegPCMAudio(
                                        executable=r"C:\Users\SetupGame\Documents\ffmpeg\ffmpeg\bin\ffmpeg.exe",
                                        source="source.mp3",
                                    )
                                )
                        except:
                            await privelage.send_private(f"{name} 9lawi ila jit", message, is_private)
                        #     pass
            if msg_splited[0] == "gol":
                to = msg_splited[1]
                text_response = " ".join(msg_splited[2:])
                for ms in client.get_all_members():
                    if to in ms.name or to.lower() == ms.name.lower():
                        await ms.send(text_response)
                        break

            # if msg == "ser":
            #     await voiceClient.disconnect()

    if "bot" in user_message:
        response = f"nta li {user_message.replace('bot','')}"
        is_private = True
        return await privelage.send_private(response, message, is_private)
