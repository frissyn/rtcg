import discord
import requests

from bot import robot
from bot import COLOR

from datetime import datetime

watcher_role = 845360539672248320


@robot.command(name="ping")
async def ping(ctx):
    await ctx.channel.trigger_typing()
    l = round(robot.latency * 1000, 2)
    em = discord.Embed(title="Pong!", color=COLOR)
    now = datetime.now().strftime("[%B %d] %I:%M %p")

    em.add_field(name="**Timestamp:**", value=f"{now}", inline=True)
    em.add_field(name="**Latency:**", value=f"{l} ms", inline=True)

    await ctx.send(embed=em)


@robot.command(name="watch")
async def toggle_watch(ctx):
    await ctx.channel.trigger_typing()
    roles = [r.id for r in ctx.author.roles]

    if watcher_role in roles:
        em = discord.Embed(
            title="Toggled Watcher Role!",
            description="You will no longer be notified of Trade Offers.",
            color=COLOR
        )

        await ctx.author.remove_roles(discord.Object(845360539672248320))
    else:
        em = discord.Embed(
            title="Toggled Watcher Role!",
            description="You will now be notified of Trade Offers.",
            color=COLOR
        )

        await ctx.author.add_roles(discord.Object(845360539672248320))
    
    await ctx.send(embed=em)


@robot.command(name="offers")
async def get_offers(ctx):
    await ctx.channel.trigger_typing()
    em = discord.Embed(
        title="Recent Trade Offers!",
        description="There are no listed trade offers right now.",
        color=COLOR
    )

    await ctx.send(embed=em)


@robot.command(name="offer")
async def send_offer(ctx, i: int, c: int):
    await ctx.channel.trigger_typing()
    r = requests.get(f"https://api.rtcg.repl.co/card/{i}")

    if r.status_code == 200:
        card = r.json()
        em = discord.Embed(
            title="Posted Trade Offer!",
            description=f"{ctx.author.name} is offering {c} of '**{card['name']}**'!",
            color=COLOR
        )

        em.set_thumbnail(url=card["image"])

        for k, v in card.items():
            if k not in ["image", "id"]:
                em.add_field(name=k.upper(), value=str(v).title(), inline=True)
    else:
        em = discord.Embed(
            title="Invalid Trade Offer!",
            description="Card you listed does not exist.",
            color=COLOR
        )

    ping = ":tada:"

    if card["rarity"] in ["Very Rare", "Legendary", "Unobtainable"]:
        ping += "<@&845360539672248320>"
    
    await ctx.send(ping, embed=em)


@robot.command(name="card")
async def card_info(ctx, i: int):
    await ctx.channel.trigger_typing()
    r = requests.get(f"https://api.rtcg.repl.co/card/{i}")

    if r.status_code == 200:
        card = r.json()
        em = discord.Embed(title="Card Info!", color=COLOR)

        em.set_thumbnail(url=card["image"])

        for k, v in card.items():
            if k == "name":
                em.add_field(name=k.upper(), value=str(v).title() + f" [{str(card['id']).zfill(4)}]", inline=True)
            elif k not in ["id", "image"] and k != "" and v != "":
                em.add_field(name=k.upper(), value=str(v).title(), inline=True)
    else:
        em = discord.Embed(
            title="Error Occured",
            description="Card you listed does not exist.",
            color=COLOR
        )
    
    await ctx.send(embed=em)


@robot.command(name="want")
async def send_want(ctx, i: int, c: int):
    await ctx.channel.trigger_typing()
    r = requests.get(f"https://api.rtcg.repl.co/card/{i}")

    if r.status_code == 200:
        card = r.json()
        em = discord.Embed(
            title="Posted Trade Listing!",
            description=f"{ctx.author.name} wants {c} of '**{card['name']}**'!",
            color=COLOR
        )

        em.set_thumbnail(url=card["image"])

        for k, v in card.items():
            if k not in ["image", "id"]:
                em.add_field(name=k.upper(), value=str(v).title(), inline=True)
    else:
        em = discord.Embed(
            title="Invalid Trade Offer!",
            description="Card you listed does not exist.",
            color=COLOR
        )

    ping = ":tada: "

    if card["rarity"] in ["Very Rare", "Legendary", "Unobtainable"]:
        ping += "<@&845360539672248320>"
    
    await ctx.send(ping, embed=em)



@robot.command(name="search")
async def card_search(ctx, param: str, query: str):
    await ctx.channel.trigger_typing()

    card = None
    r = requests.get(f"https://api.rtcg.repl.co/cards")
    em = discord.Embed(
        title="Error Occured",
        description="Couldn't find the card you're looking for!",
        color=COLOR
    )

    if r.status_code == 200:
        cards = r.json()
        em = discord.Embed(title="Card Search!", color=COLOR)

        for card in cards:
            if str(card[param.lower()]).lower() == query.lower():
                card = card
            else:
                card = None

        if card != None:
            em = discord.Embed(title="Card Search!", color=COLOR)
            em.set_thumbnail(url=card["image"])
            for k, v in card.items():
                if k == "name":
                    em.add_field(name=k.upper(), value=str(v).title() + f" [{str(card['id']).zfill(4)}]", inline=True)
                elif k not in ["id", "image"] and k != "" and v != "":
                    em.add_field(name=k.upper(), value=str(v).title(), inline=True)
    
    await ctx.send(embed=em)
