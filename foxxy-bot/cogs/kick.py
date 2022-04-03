import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
from cogs.utils.invalidperms import invalidpermissions

class kick(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def kick(self, ctx:commands.Context, member: nextcord.Member, *, reason = None):
        #g = ctx.guild
        if member == None:
            await ctx.send("Please specify a user to kick!")
        elif member == ctx.author:
            await ctx.send("You can't kick yourself!")
        else:
            if not ctx.message.author.guild_permissions.mute_members:
                invalidpermissions(ctx)
            else:
                await member.kick(reason=reason)
                embed=nextcord.Embed(title="Kick Command", description="", color=0xff0000)
                embed.add_field(name="Offender", value=str(member), inline=False),
                embed.add_field(name="Reason", value=reason, inline=False),
                embed.add_field(name="Moderator", value=ctx.message.author, inline=False)
                await ctx.send(embed=embed)
                

def setup(bot: commands.Bot):
    bot.add_cog(kick(bot))