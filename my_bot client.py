#Import discord package
import discord
from discord.ext import commands
#Client
client = discord.Client()

@client.event
async def on_ready():
    bot_channel = client.get_channel(777714377281241098)
    await bot_channel.send("I'm alive!")


@client.event
async def on_message(message):
    if message.content == "give me version":
        bot_channel = client.get_channel(777714377281241098)

        myEmbed = discord.Embed(
            title="Current Version",
            description="The bot is in Version 1.0.0",
            color=0x00ff00       
        )
        myEmbed.add_field(
            name="Version Code:",
            value="v.1.0.0",
            inline="false"
        )
        myEmbed.add_field(
            name="Date Released:",
            value="14th Nov 2020",
            inline="false"
        )
        myEmbed.set_author(name="George")
        myEmbed.set_footer(text="This is a footer")
        myEmbed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQBhlFTyGVD3-D_v3ujqaJewDN37ZasDwjRtw&usqp=CAU")
        myEmbed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQBhlFTyGVD3-D_v3ujqaJewDN37ZasDwjRtw&usqp=CAU")

        await bot_channel.send(embed=myEmbed)


#Run the client on the server
client.run('Nzc3NzEwMTYyMjE5MTA2MzE1.X7HZBw._Im9KUUcJ_T3JrJyHAfkHuFcmTI')