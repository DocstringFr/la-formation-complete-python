import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.members = True  # Vous devez activer les intents dans les paramètres du Bot
bot = commands.Bot(command_prefix="!", intents=default_intents)


@bot.event
async def on_ready():
    print("Le bot est connecté.")


@bot.event
async def on_member_join(member):
    print(f"Un nouveau membre est arrivé : {member.display_name}")


@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()

    for each_message in messages:
        await each_message.delete()


bot.run(os.getenv("TOKEN"))
