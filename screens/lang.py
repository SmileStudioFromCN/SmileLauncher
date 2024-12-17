import json

def lang():
    with open('../lang.json', 'r') as f:
        config = json.load(f)
        return config['lang']