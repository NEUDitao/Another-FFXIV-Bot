import requests
import json
import discord

# TODO: Handle Errors well


async def handle_iam(message: discord.Message):
    msg = message.content.split()

    if len(msg) != 2 and len(msg) != 4:
        # TODO: add embed telling people what the proper parameters are
        await message.channel.send("Improper use of iam!")

    if len(msg) == 2:
        if (isinstance(id) is not int):
            await message.channel.send("Big Error Bitch")
            return
        id = msg[1]

    if len(msg) == 4:
        world = msg[1]
        forename = msg[2]
        surname = msg[3]
        response = requests.get(
            "https://xivapi.com/character/search?name=" + forename + "%20" + surname + "&server=" + world)
        body = json.loads(response.text)
        if len(body['Results']) != 1:
            await message.channel.send("Big Error Bitch")
            return

        id = str(body['Results'][0]['ID'])

    response = requests.get("https://xivapi.com/character/" + id)
    body = json.loads(response.text)

    embed_title = body['Character']['Name'] + \
        ' (' + body['Character']['Server'] + ')'
    embed_description = """
    I've successfully saved your character TODO:

    **Nickname**
    Your Discord Name will be changed to TODO:

    **Roles Added**
    TODO:
    """

    embed = discord.Embed(
        title=embed_title,
        description=embed_description,
        colour=discord.Colour.green()
    )
    embed.set_thumbnail(url=body['Character']['Avatar'])

    await message.channel.send(embed=embed)
