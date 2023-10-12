async def join(client):
    try:
        await client.join_chat("SiArab_Support")
        await client.join_chat("Jasasiab")
    except BaseException:
        pass
