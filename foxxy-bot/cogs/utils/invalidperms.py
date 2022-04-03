import nextcord
from nextcord.ext import commands


def invalidpermissions(ctx):
    embed=nextcord.Embed(title="Invalid Permissions", description="You do not have the required permissions to execute this command!", color=0xff0000)
    ctx.send(embed=embed)