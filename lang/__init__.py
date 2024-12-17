import json

def lang():
    with open('lang.json', 'r') as f:
        config = json.loads(f.read())
        return config['lang']