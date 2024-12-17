# copyright (c) 2024 Smile Studio

# run this file to start the program.

from screens import startScreen
from screens import mainScreen
import json

try:
    config = open("config.json", "r")
    config_data = json.loads(config.read())
    config.close()
except FileNotFoundError:
    startScreen.run()
else:
    mainScreen.mainWindow(config_data)