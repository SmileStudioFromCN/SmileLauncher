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
    config_data = startScreen.run()
    config = open("config.json", "w")
    write_data = json.dumps(config_data)
    config.write(write_data)
    config.close()
else:
    mainScreen.mainWindow(config_data)