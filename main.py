import discord
from discord.ext import commands
import asyncio
from colorama import Fore, init

init(autoreset=True)

# made by @stefkeefr on github!

token = "YOUR_TOKEN_HERE"
ltc_address = None
snipe_cache = {}
typing_task = None

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",", self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(Fore.GREEN + f"[INFO] Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message_delete(message):
    snipe_cache[message.channel.id] = message


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! `{round(bot.latency * 1000)}ms`")

@bot.command()
async def spam(ctx, count: int, *, message: str):
    if count > 30:
        await ctx.send("Limit is 30 messages.")
        return
    for _ in range(count):
        await ctx.send(message)
        await asyncio.sleep(0.3)

@bot.command()
async def ltc(ctx):
    global ltc_address
    if not ltc_address:
        await ctx.send("LTC address is not set. Use `,setltc <address>`.")
    else:
        await ctx.send(f"LTC Address: `{ltc_address}`")

@bot.command()
async def setltc(ctx, *, address: str):
    global ltc_address
    ltc_address = address
    await ctx.send(f"LTC address set to `{ltc_address}`")

react_targets = {}

@bot.command()
async def autoreact(ctx, user: discord.User, emoji: str):
    react_targets[user.id] = emoji
    await ctx.send(f"Now auto-reacting to {user.name}'s messages with {emoji}")

@bot.command()
async def reactoff(ctx):
    react_targets.clear()
    await ctx.send("Auto-react disabled.")

@bot.event
async def on_message(message):
    if message.author.id in react_targets and message.author != bot.user:
        try:
            await message.add_reaction(react_targets[message.author.id])
        except:
            pass
    await bot.process_commands(message)

@bot.command()
async def cmds(ctx):
    cmds = """
`ping` - Bot latency  
`spam <count> <message>` - Spam message (limit 30)  
`setltc <address>` - Set LTC address  
`ltc` - Show LTC address  
`autoreact <user> <emoji>` - Auto-react to a user's messages  
`reactoff` - Disable auto-react  
`userinfo <@mention/id>` - Show user info  
`snipe` - Show last deleted message  
`typing` - Start fake typing  
`stoptyping` - Stop fake typing  
`purge <count>` - Delete your messages  
`dm <user_id> <text>` - Send DM to user  
"""
    await ctx.send(cmds)

@bot.command()
async def userinfo(ctx, user: discord.User = None):
    user = user or ctx.author
    embed = discord.Embed(title=f"{user}", color=discord.Color.blurple())
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.add_field(name="Bot?", value=user.bot, inline=False)
    embed.add_field(name="Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def snipe(ctx):
    msg = snipe_cache.get(ctx.channel.id)
    if msg:
        await ctx.send(f"Sniped: `{msg.author}`: {msg.content}")
    else:
        await ctx.send("Nothing to snipe!")

@bot.command()
async def typing(ctx):
    global typing_task
    if typing_task:
        await ctx.send("Already typing.")
        return

    async def fake_typing():
        while True:
            async with ctx.typing():
                await asyncio.sleep(10)

    typing_task = asyncio.create_task(fake_typing())
    await ctx.send("Typing started...")

@bot.command()
async def stoptyping(ctx):
    global typing_task
    if typing_task:
        typing_task.cancel()
        typing_task = None
        await ctx.send("Typing stopped.")
    else:
        await ctx.send("Typing was not active.")

@bot.command()
async def purge(ctx, count: int):
    async for msg in ctx.channel.history(limit=100):
        if msg.author == bot.user:
            try:
                await msg.delete()
                count -= 1
                if count <= 0:
                    break
            except:
                pass

@bot.command()
async def dm(ctx, user_id: int, *, text: str):
    user = bot.get_user(user_id)
    if user:
        try:
            await user.send(text)
            await ctx.send(f"DM sent to {user.name}")
        except:
            await ctx.send("Couldn't send DM. They may have DMs closed.")
    else:
        await ctx.send("User not found.")

# -----------

bot.run(token, bot=False)
