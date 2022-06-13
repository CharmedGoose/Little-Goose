import discord
import os
from discord.ext import commands, tasks
import random

intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)

client = commands.Bot(command_prefix='g!', intents=discord.Intents.all())

starter = ["Did Anyone See The New Never Gonna Give You Up Animated Video?",
           "Did You Know Rick Astley Made Other Good Songs Like Keep Singing?",
           "Gif Or Jif?"
           ]


@tasks.loop(minutes=5)
async def spam_poop():
    channel = client.get_channel(973935616846880819)
    await channel.send("*poop*")
    await channel.send("*eats poop*")


@client.event
async def on_message(message):
    if ("<@465097356874874881>" in message.content):
        await message.channel.send(
            "This void consumes me.")
    if ("<@851537359588818944>" in message.content
            or "<@984459311587655690>" in message.content):
        await message.channel.send("Don't hurt goose")
    if (":dead:" in message.content):
        await message.channel.send(random.choice(starter))
    await client.process_commands(message)


@client.event
async def on_ready():
    spam_poop.start()


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded The {extension} Cog")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded The {extension} Cog")


@client.command()
async def reload(ctx, extension):
    message = await ctx.send(f"Reloading The {extension} Cog")
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await message.edit(content=f"Reloaded The {extension} Cog")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}")


client.run(
    'OTg0NDU5MzExNTg3NjU1Njkw.Gi5XJw.GVPEXpEhwN7BUZEMNVLamMsBVudnQxd87SInr0')
