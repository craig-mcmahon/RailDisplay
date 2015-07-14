import json
import time

from RailDisplay import RailDisplay

with open('example-config.json') as config_file:
    config = json.load(config_file)

railDisplay = RailDisplay(config)
while True:
    railDisplay.update_board()
    time.sleep(20)
