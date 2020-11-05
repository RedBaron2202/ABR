import discord
from discord.ext import commands
from discord import User
from discord import Message
from asyncio import sleep

import requests
import json

"""
This section has required info to connect to Wrike:
api_version,
Id of Wrike fodler,
Url
And your Permanent token for autharization
"""
api_version = 4

folder_id = <Wrike folder id>

url = f"https://www.wrike.com/api/v{api_version}/folders/{folder_id}/tasks"

headers = {<your token is here>}


#setting command prefix for discord, can be anything

client = commands.Bot(command_prefix="!")

#messages for users, can be translated to any preffered language
success = "Successfully reported bug!"
error = "Unexpected error, try later!"
formatError = "Wrong format!"


#Loading event, when bot successfully loaded it will bring message 
#to the console
@client.event
async def on_ready():
    print("Bot is ready")


#Bug report command itself starts here
#to use it, type in Discord chat: "!bug <name>:<description>(optional)
@client.command(name="bug")
async def bug(ctx, text: str):

    #Try catch loop in case user will make mistake
    try:
        title, description = text.split(":")
    except Exception:
        await ctx.send(formatError)
    else:

	#User arguments transformed into one dictionary
        data = {}
        data['title'] = title
        data['description'] = description
    	
	#Post request itself
        r = requests.post(url, headers = headers, data = data)
       
        #In case operation was successfull(code 200)
        #User will recieve notification in Discord
        #Otherwise user will recieve error in Discord
        print(r.status_code)
        if r.status_code == 200:
            await ctx.send(success)
        else:
            await ctx.send(error)
    
#Here you should put your Discord bot token
client.run("<Discord token here>");
