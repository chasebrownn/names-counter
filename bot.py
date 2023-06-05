import discord
from dotenv import load_dotenv  
import os
import getNames
import time

load_dotenv() 
TOKEN = os.getenv('BOT_TOKEN')

def run_discord_bot():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        channel = client.get_channel(1107808231662821390)
        print(channel)
        
        while True:
            numNames = getNames.getAmountNamesRegistered()
            new_name = f"Names: {numNames}"
            await channel.edit(name=new_name)
            time.sleep(60)


    client.run(TOKEN)