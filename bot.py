import discord
from discord.ext import commands
from discord import User
from discord import Message
from asyncio import sleep

import requests
import json

api_version = 4

folder_id = "IEAD7MPLI4RR73ER"

url = f"https://www.wrike.com/api/v{api_version}/folders/{folder_id}/tasks"

headers = {
    'authorization': "bearer eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjQxNzQzMTUsXCJpXCI6NzMwMjA3MyxcImNcIjo0NjIyNTM4LFwidVwiOjkzODA4ODQsXCJyXCI6XCJVU1wiLFwic1wiOltcIldcIixcIkZcIixcIklcIixcIlVcIixcIktcIixcIkNcIixcIkRcIixcIk1cIixcIkFcIixcIkxcIixcIlBcIl0sXCJ6XCI6W10sXCJ0XCI6MH0iLCJpYXQiOjE2MDQ1MzA2MDZ9.s0wRI2bsDYB77ntDDfgn9U97EIfQkGM6sm3vp1P-n9k",
}

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(name="bug")
async def bug(ctx, text: str):
    try:
        title, description = text.split(":")
    except Exception:
        await ctx.send("Непраильный формат!")
    else:
        data = {}
        data['title'] = title
        data['description'] = description
    
        r = requests.post(url, headers = headers, data = data)
        print(r.status_code)
        if r.status_code == 200:
            await ctx.send("Баг репорт отправлен успешно!")
        else:
            await ctx.send("Произошла ошибка! Попробуете позже!")
    

client.run("NzczNjYzMjMwODc3ODkyNjE5.X6MgCA.cfOghycMBOGwXfC_m7wlqCaKKXY");