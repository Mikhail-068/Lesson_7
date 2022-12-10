import yaml


text = {'Mondey': ['Молоко', "Батон"],
    "Tuesday": ["Кефир", "шоколад"]}

with open('buy.yaml', 'w') as f:
    yaml.dump(text, f)