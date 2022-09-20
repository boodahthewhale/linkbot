
from turtle import color
import discord
from discord.ext import commands
import discord.embeds

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)



@bot.command()
async def ms(ctx):
    await ctx.send(f'ms = {round(bot.latency * 1000)}ms ')

@bot.command()
async def links(ctx):
    embed=discord.Embed(title="media", description="here are all the media for this person", color=discord.Color.blue(),)
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="YOUTUBE", value="https://youtube.com", inline=False)
    embed.add_field(name='TWITCH', value="https://twitch.com",inline=False)
    embed.add_field(name='INSTAGRAM', value='https://instagram.com', inline=False)
    await ctx.send(embed=embed)


bot.run("your bot token here")
