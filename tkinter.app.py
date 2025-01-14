import tkinter as tk
from tkinter import messagebox


Igbo_dict = {
    'Bia': 'come',
    'Mmirri': 'water',
    'Gawa': 'go',
    'Mmanu': 'oil',
    'otutu': 'morning',
    'walli': 'take',
    'ntutu': 'hair',
    'akwa': 'cloth',
    'Awu': 'goat',
    'Nnkita': 'Dog',
    'Nwa': 'child',
    'Anwu': 'sun',
    'Nwoke': 'brother',
    'Bata': 'enter',
    'Biko': 'please',
    'Echi': 'tomorrow',
    'Ashhia': 'market',
    'Okporoko': 'stockfish',
    'Oge': 'time',
    'Eze': 'king',
}

Igala_dict = {
    'good morning': 'olodudu',
    'thanks': 'agba',
    'come': 'lia',
    'go': 'lo',
    'god': 'ojo',
    'eat': 'jeun',
    "one": "oka",
    'two': 'eji',
    'twins': 'ogwu',
    'floor': 'ane',
    'three': 'eta',
    'room': 'ejefu',
    'kitchen': 'obuka',
    'leg': 'ere',
    'who': 'ene',
    'love': 'ufedo',
    'water': 'omi',
    'head': 'oji',
    'bed': 'ate',
    'amen': 'ami'
}

Ijaw_dict = {
    'water': 'ame',
    'land': 'anj',
    'fish': 'bere',
    'tree': 'diro',
    'house': 'eke',
    'sky': 'feru',
    "one": "oka",
    'boat': 'ibe',
    'food': 'ine',
    'moon': 'kpereke',
    'stone': 'kpo',
    'room': 'ejefu',
    'kitchen': 'moto',
    'sun': 'oku',
    'gold': 'ola',
    'river': 'piri',
    'bird': 'temo',
    'forest': 'wuo',
    'love': 'yin',
    'peace': 'ziri'
}

Efik_dict = {
    'good morning':'emesire',
    'please':'daiya',
    'sorry':'kpe',
    'dog' : 'ewa',
    'thankyou':'sosono',
    'goat': 'ebot',
    'bread': 'uyo',
    'God':'Abasi',
    'bye':'kaadi',
    'sleep':'daiya',
    'five':'ition',
    'witch':'ifot',
    'water':'mmoon',
    'seven':'itiaba',
    'love': 'ima',
    'joy':'idara',
    'grace':'mfon',
    'lion':'ekpe',
    'door':'usun',
    'war':'ekon',
}


French_dict = {
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



root = tk.Tk()
root.title("Dictionary App")
root.geometry("500x400")

selected_dict = tk.StringVar()
word_input = tk.StringVar()

def get_meaning():
    word = word_input.get().strip().lower()
    dictionary_name = selected_dict.get()

    if dictionary_name in dictionaries and word in dictionaries[dictionary_name]:
        meaning = dictionaries[dictionary_name][word]
        result_label.config(text=f"Meaning of '{word}':\n{meaning}")

    else:
         result_label.config(text=f"sorry, the word '{word}'was not found in the selected dictionary.")

label = tk.Label(root, text="Choose a Dictionary:", font=("Arial", 18))
label.pack(pady=10)

dict_menu = tk.OptionMenu(root, selected_dict, *dictionaries.keys())
dict_menu.pack(pady=10)

word_label = tk.Label(root, text="Enter a word:", font=("Arial", 14))
word_label.pack(pady=10)

word_entry = tk.Entry(root, textvariable=word_input, font=("Arial", 16))
word_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Interpretation", font=("Arial", 14), command=get_meaning)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), justify=tk.LEFT)
result_label.pack(pady=20)

root.mainloop()


