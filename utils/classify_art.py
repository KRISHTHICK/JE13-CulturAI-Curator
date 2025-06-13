import random

def identify_artifact(img):
    options = [
        {"style": "Mughal", "region": "India", "description": "Mughal art blends Persian, Indian, and Islamic influences."},
        {"style": "Ukiyo-e", "region": "Japan", "description": "Ukiyo-e is a genre of Japanese woodblock prints and paintings."},
        {"style": "Romanesque", "region": "Europe", "description": "Characterized by semi-circular arches and thick walls."},
        {"style": "Chola Bronze", "region": "Tamil Nadu, India", "description": "Sacred Hindu sculptures from Chola dynasty."}
    ]
    return random.choice(options)  # Replace with model later
