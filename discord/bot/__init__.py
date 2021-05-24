import os
import discord

from discord.ext import commands

COLOR = 0x9370DB
TOKEN = os.environ["BOT_TOKEN"]
INTENTS = discord.Intents.default()
INTENTS.members = True
INTENTS.presences = True

robot = commands.Bot(command_prefix="r! ", intents=INTENTS)

from .comms import *
from .events import *