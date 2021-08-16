import discord 
import youtube_dl
from discord.ext import commands, tasks
from random import choice
import os
####################################################################################
#zaruri commands

client = commands.Bot(command_prefix="+")

####################################################################################
#declare your variables here

status=['Epic shit','With zindagi','Music','with my toys']
responses=['kya kar raha hai bsdk?','phir se aagaya tu?','aur bhai kaisa hai?','arey arey yeh kaun aagaya chiii!','areey sir aap yaha kaise?']
pickups=['Are you wi-fi? Cause I\'m totally feeling a connection.','If I had a nickel for every time I saw someone as beautiful as you, I\'d have five cents.','I\'d like to take you to the movies, but they don\'t let you bring in your own snacks.']
####################################################################################
#General commands

@client.event
async def on_ready():
    change_status.start()
    print("Bot tayar hai")

@client.command(name="hello", help="This command gives random responses to your greetings")
async def hello(ctx):
    await ctx.send(+choice(responses))
    
@client.command(name="pickup", help="Yeh command tumpe line marega")
async def pickup(ctx):
    await ctx.send("Rohan says: "+choice(pickups))

@client.command()
async def nothing(ctx):
    await ctx.send("kaam karle kuch khali admi")

@client.command()
async def fuckoff(ctx):
    await ctx.send("zayada mat bol saleyy")

#################################################################################################
#Presentation wali shit

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

#################################################################################################
#Music commands

@client.command()
async def play(ctx, url: str):
    voiceChannel= discord.utils.get(ctx.guild.voice_channels, name='General')
    voice= discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voiceChannel.connect() 
    await ctx.send("hello doston mai aagaya")

@client.command()
async def leave(ctx):
    voice= discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("aacha toh hum chalte hai")

@client.command()
async def pause(ctx):
    voice= discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Kuch baj hi nahi raha roku kya?")

@client.command()
async def resume(ctx):
    voice= discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Rok toh sahi pehele gana")

@client.command()
async def stop(ctx):
    voice= discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send("Mujhe sahi mei rok rahe ho tum?")
    voice.stop()


##################################################################################################
#End line

client.run("ODM4MzE1NjI3MDIxMjA1NTA2.YI5URA.NEtNyO3cxRAJ61EoKf24oZVklWQ")
