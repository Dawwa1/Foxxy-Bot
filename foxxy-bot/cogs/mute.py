import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
from cogs.utils.invalidperms import invalidpermissions
import asyncio

class mute(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def mute(self, ctx:commands.Context, member: nextcord.Member, length = None, *, reason = None):
        g = ctx.guild
        role = get(g.roles, name="muted")
        lengthm = length*60
        if member == None:
            await ctx.send("Please specify a user to mute!")
        elif member == ctx.author:
            await ctx.send("You can't mute yourself!")
        else:
            if not ctx.message.author.guild_permissions.mute_members:
                invalidpermissions(ctx)
            else:
                if not role in g.roles:
                    perms = nextcord.Permissions(send_messages=False, read_messages=True)
                    role = await g.create_role(name='muted', permissions=perms)
                    return
                else:
                    await member.add_roles(role)
                    embed=nextcord.Embed(title="Mute Command", description="", color=0xff0000)
                    embed.add_field(name="Offender", value=str(member), inline=False),
                    embed.add_field(name="Length", value=str(length) + " minutes", inline=False),
                    embed.add_field(name="Reason", value=reason, inline=False),
                    embed.add_field(name="Moderator", value=ctx.message.author, inline=False)
                    await ctx.send(embed=embed)
                    await asyncio.sleep(int(lengthm))
                    await member.remove_roles(role)
                    embed=nextcord.Embed(title="Auto Unmute", description="", color=0xff0000)
                    embed.add_field(name="Offender", value=str(member), inline=False),
                    embed.add_field(name="Length", value=str(length) + " minutes", inline=False),
                    embed.add_field(name="Reason", value=reason, inline=False),
                    embed.add_field(name="Moderator", value=ctx.message.author, inline=False)
                    await ctx.send(embed=embed)
                    
    @commands.command()
    async def unmute(self, ctx:commands.Context, member: nextcord.Member, *, reason = None):
        g = ctx.guild
        role = get(g.roles, name="muted")
        if member == None:
            await ctx.send("Please specify a user to unmute!")
        elif member == ctx.author:
            await ctx.send("You can't unmute yourself!")
        else:
            if not ctx.message.author.guild_permissions.mute_members:
                invalidpermissions(ctx)
            else:
                await member.remove_roles(role)
                embed=nextcord.Embed(title="Unmute", description="", color=0xff0000)
                embed.add_field(name="Offender", value=str(member), inline=False),
                embed.add_field(name="Reason", value=reason, inline=False),
                embed.add_field(name="Moderator", value=ctx.message.author, inline=False)
                await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(mute(bot))