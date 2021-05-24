from bot import TOKEN
from bot import robot

from web import server

server.start()
robot.run(TOKEN)