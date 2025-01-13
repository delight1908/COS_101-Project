# French-English dictionary with 20 words
french_dict = {
    "bonjour": "hello",
    "amour": "love",
    "maison": "house",
    "chat": "cat",
    "chien": "dog",
    "voiture": "car",
    "arbre": "tree",
    "eau": "water",
    "pain": "bread",
    "école": "school",
    "livre": "book",
    "merci": "thank you",
    "pomme": "apple",
    "sourire": "smile",
    "beau": "beautiful",
    "ami": "friend",
    "fleur": "flower",
    "porte": "door",
    "fenêtre": "window",
    "soleil": "sun"
}

# Function to translate a French word to English
def translate_to_english(french_word):
    return french_dict.get(french_word.lower(), "Word not found in the dictionary.")

# Example of using the dictionary
french_word = input("Enter a French word: ").lower()
english_translation = translate_to_english(french_word)
print(f"The English translation of '{french_word}' is: {english_translation}")
