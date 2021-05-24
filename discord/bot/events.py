import discord

from bot import robot


@robot.event
async def on_ready():
    robot.remove_command("help")
    
    game = discord.Game("Replit Trading Card Game")
    await robot.change_presence(status=discord.Status.online, activity=game)

    print(f"{robot.user.name} has connected to Discord")
