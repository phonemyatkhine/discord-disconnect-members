  
import discord
import keyboard
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    channel = discord.utils.get(bot.get_all_channels(), name='general')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.command()
async def kick(ctx, member: discord.Member):
    admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
    unkick_quotes = [
        'You cannot kick Mod or Admin :Pepeg:',
        'No u :Gottem:',
        ':ezsadge:'
    ]
    for role in member.roles:
        if role.name == "Admin" or role.name == "Mod":
            response = random.choice(unkick_quotes)
            await ctx.channel.send(response)
            await ctx.message.author.move_to(None)
            return 
    kick_qoutes = [
        'Bye :Gottem:',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Bye Kalay apahy :Pepelook:',
        'Talk shit get kicked :BASED:',
        'Retard alert :Pepeg:',
        'You propably deserved it',
        'Get your revenge by using !kick'
    ]
    response = random.choice(kick_qoutes)
    await ctx.channel.send(response)
    await member.move_to(None)

# @bot.command()
# async def kick_wyk(ctx):
#     user_id = "302747056835919873"
#     user = await bot.fetch_user(user_id)
#     await kick(user)
bot.run("ODc4MzU0NDU1MDIyNjgyMTIz.YR_9VQ.mFEoXQ-1RUV1e74vje6alwdFPZg")
