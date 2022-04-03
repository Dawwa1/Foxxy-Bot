import os
from dotenv import load_dotenv
import nextcord
import json
import os
from nextcord.ext import commands
from cogs.utils.vars import welcomechannel

os.chdir(r"C:\Users\Vova\Desktop\projects\foxxy-bot")

def main():
    intents = nextcord.Intents().all()
    client = commands.Bot(command_prefix="!", help_command=None, activity=nextcord.Game(name="in the mud"), intents=intents)

    load_dotenv()

    testingServer = 924763015872671794

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    @client.event
    async def on_member_join(member):
        welcomechannel.send("Welcome!")

    # loads all the cogs in cogs folder
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')

    client.run(os.getenv("BOT"))

if __name__ == '__main__':
    main()