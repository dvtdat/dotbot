import discord

TOKEN = "MTA2MTIzMDA5ODY0MjEwODQyNg.G7Zp-i.SkKiF_fLKiSRNvDfhJg-jsKuKz8qBm4CXk6zj8"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".hello"):
        await message.channel.send("lo con cac")

    if message.content.startswith(".goodbye"):
        await message.channel.send("khong ai nhan tin nen di ngu? chu' j 🙄")

    if message.content.startswith("da. god"):
        await message.channel.send("toi qua' gae")

client.run(TOKEN)