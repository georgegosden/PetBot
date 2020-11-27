#Import discord package
import json
import discord
from discord.ext import commands

#Get all the stuff from the json file
jsonfile = open('bot_data.json', 'r')
bot_data = jsonfile.read()

bot_data_obj = json.loads(bot_data)
bot_token = bot_data_obj['token']
bot_version = bot_data_obj['version']
bot_channel = int(bot_data_obj['bot_channel'])

#Client
client = commands.Bot(command_prefix='ly.')

@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(
        title="Current Version",
        description="The bot is in Version: {}".format(bot_version),
        color=0x00ff00       
        )
    myEmbed.add_field(
        name="Version Code:",
        value="v.{}".format(bot_version),
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
    
    await context.message.channel.send(embed=myEmbed)

@client.command(name='testmessage')
async def testmessage(context):
    await context.message.author.send('Test message')




@client.event
async def on_ready():
    testing_channel = client.get_channel(bot_channel)
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Life S22E13"))
    await testing_channel.send("I'm alive!")



#Run the client on the server
client.run(bot_token)