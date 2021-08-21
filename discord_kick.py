  
from os import name
import discord
import keyboard
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    channel = discord.utils.get(bot.get_all_channels(), name='general')
    # guild = discord.utils.get(bot.get_guild(), id = "415188177020518411")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.command()
async def kick(ctx, member: discord.Member):
    unkick_quotes = [
        'You cannot kick Admin or Mod <:PepeMods:859799773045063690>',
        'No u <:PepeLaugh:858934854355386388>',
        '<:GigaChad:871288344947097640>',
        '<:KEKL:701113461027110954>',
        'Mess with the owner get the boner <:monkaO:736699592648818861>'
    ]
    for role in member.roles:
        if role.name == "Admin" or role.name == "Mod":
            response = random.choice(unkick_quotes)
            await ctx.channel.send(response)
            await ctx.message.author.move_to(None)
            return
    kick_qoutes = [
        'Bye <:Gottem:792842042127548416>',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Talk shit get kicked <:BASED:763743513702694913>',
        'Retard alert <:Pepeg:706008435044646942>',
        'You probably deserved it <:EZsadge:859273083806679040>',
        'Get your revenge by using !kick <:WeirdChamp:705020603987525643>',
        'POV: You are someone\'s child <:Weirdge:859273108056834050>',
        'Reeeeeeeeee <:REEEEEeeee:709099147860639814>',
        '<:WTFF:705022139471888455>',
        'Amogus <:Susge:857360771359965194> '
    ]
    response = random.choice(kick_qoutes)
    await ctx.channel.send(response)
    await member.move_to(None)

@bot.command()
async def sus(ctx, member: discord.Member):
    vc_channel = discord.utils.get(bot.get_all_channels(), name='Among Us')
    unkick_quotes = [
        '<:Susge:857360771359965194>'
    ]
    for role in member.roles:
        if role.name == "Admin" or role.name == "Mod":
            response = random.choice(unkick_quotes)
            await ctx.channel.send(response)
            await ctx.message.author.move_to(vc_channel)
            return
    kick_qoutes = [
        '<:Susge:857360771359965194>',
    ]
    response = random.choice(kick_qoutes)
    await ctx.channel.send(response)
    await member.move_to(vc_channel)

@bot.command()
async def kick_wyk(ctx):
    user_id = "302747056835919873"
    guild = bot.get_guild(415188177020518411)
    user = await guild.fetch_member(672075757203357698)
    kick_qoutes = [
        'Bye kalay aphay <:Gottem:792842042127548416>',
        'Talk shit get kicked <:BASED:763743513702694913>',
        'Retard WYK <:Pepeg:706008435044646942>',
        'You probably deserved it <:EZsadge:859273083806679040>',
        'POV: You are WYK\'s child <:Weirdge:859273108056834050>',
        'Reeeeeeeeee <:REEEEEeeee:709099147860639814>',
        '<:WTFF:705022139471888455>',
        'Amogus <:Susge:857360771359965194> '
    ]
    response = random.choice(kick_qoutes)
    await ctx.channel.send(response)
    await user.move_to(None)

@bot.command()
async def help_kick_bot(ctx):
    embed = discord.Embed(
        title = "Kick Retards Bot Help",
        color = discord.Color.blue(),
        description = "Help command for kick retards bot."
    )
    embed.set_thumbnail(url="https://i.ytimg.com/vi/SEQc0A3jM9A/maxresdefault.jpg")
    embed.add_field(name="**Kick User**", value="Kick annoying users with ```!kick @<username> ``` ", inline=False)
    embed.add_field(name="**Sus User**", value="Move annoying users to Among US channel with ```!sus @<username> ``` ", inline=False)
    embed.add_field(name="**Kick WYK**", value="Kick fucking idiot WYK ```!kick_wyk``` ", inline=False)
    embed.add_field(name="ENJOY", value="Admin and Mod work hard to keep the server happy and content \n Happy Kicking <:OkayChamp:696037164911165562> <:PepeMods:859799773045063690> ")
    response =  'Kick annoying users with "!kick @<username>" command.\nMove annoying users to Among Us channel with "!sus @<username>" command.\nOur generous Admin and Mod works hard to keep the server happy and content <:PepeMods:859799773045063690>\nHappy Kicking <:OkayChamp:696037164911165562> '
    await ctx.channel.send(embed=embed)

@bot.command()
async def id(ctx, member : discord.Member):
    await ctx.channel.send(member.id)
bot.run("ODc4MzU0NDU1MDIyNjgyMTIz.YR_9VQ.5LGwdtP2mQSsvDanAr4HUB_Z-Cw")
