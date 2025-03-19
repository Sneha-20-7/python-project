import random
from PIL import Image, ImageTk
import os
import tkinter as tk
import pygame

# Initialize window
window = tk.Tk()
window.title("Pictionary")
window.geometry("900x900")

# Initialize pygame for music
pygame.mixer.init()
music_path = r'C:\Users\SNEHA\Desktop\python\Python-practice\project4\music\Alphabet Parade.mp3'

if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
else:
    print("Music file not found.")

# Create gradient background using canvas
canvas = tk.Canvas(window, width=900, height=900)
canvas.pack(fill="both", expand=True)

def create_gradient():
    for i in range(900):
        color = f"#{int(255 * (i / 900)):02x}{int(120 + 135 * (i / 900)):02x}FF"
        canvas.create_line(0, i, 900, i, fill=color)

create_gradient()

# Alphabetical association
Pictionary = [
    "Apple", "Ball", "Cat", "Dog", "Elephant", "Fox", "Grapes",
    "Hat", "Ice", "Jellyfish", "King", "Lion", "Mango", "Nest", "Owl",
    "Peacock", "Queen", "Rabbit", "Sun", "Toy", "Umbrella", "Violin", 
    "Whale", "Xylophone", "Yak", "Zebra"
]

guesses = 0

# UI Elements
label = tk.Label(window, text="Pictionary: Guess the object!", font=("Comic Sans MS", 24), bg="#FFD1DC", fg="#6A0572")
canvas.create_window(450,80, window=label)

entry = tk.Entry(window, font=("Comic Sans MS", 18), bg="#FFF5BA", fg="#FF1493", justify="center")
canvas.create_window(450, 600, window=entry)

result_label = tk.Label(window, text="", font=("Comic Sans MS", 18), fg="#00CED1")
canvas.create_window(450, 665, window=result_label)

border_frame = tk.Label(window, bg="red")
canvas.create_window(450, 350, window=border_frame, width=430, height=430)

image_label = tk.Label(window, bg="#FFD1DC")
canvas.create_window(450, 350, window=image_label)

# High Score Management
high_score_path = 'hiscore.txt'

def get_high_score():
    if os.path.exists(high_score_path):
        with open(high_score_path, 'r') as f:
            hiscore = f.read().strip()
            return int(hiscore) if hiscore else float('inf')
    return float('inf')

def set_high_score(score):
    with open(high_score_path, 'w') as f:
        f.write(str(score))

def load_new_image():
    global selected_object, guesses
    guesses = 0
    selected_object = random.choice(Pictionary)
    print(f"Selected Object (for debugging): {selected_object}")
    image_path = os.path.join(r'C:\Users\SNEHA\Desktop\python\Python-practice\project4\images', f"{Pictionary.index(selected_object) + 1}.jpg")
    
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            image = image.resize((400, 400))
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
    else:
        print(f"Error: Image not found at path: {image_path}")

load_new_image()

def check_guess():
    global guesses
    user_guess = entry.get().strip().capitalize()
    guesses += 1

    if user_guess == selected_object:
        result_label.config(text=f"🎉 Correct! You guessed it in {guesses} attempts! 🎉", fg="#32CD32")
        high_score = get_high_score()
        if guesses < high_score:
            set_high_score(guesses)
            result_label.config(text=f"🎉 New High Score! You guessed it in {guesses} attempts! 🎉", fg="#FFD700")
        window.after(2000, load_new_image)
    else:
        result_label.config(text="❌ Wrong guess! Try again.", fg="#FF4500")

# Submit button
submit_button = tk.Button(window, text="Submit", command=check_guess, bg="#9400D3", fg="#FFFFFF", font=("Comic Sans MS", 18))
canvas.create_window(450, 740, window=submit_button)

# Border Animation
def animate_border():
    colors = ["#FF1493", "#FFD700", "#00CED1", "#9400D3", "#32CD32"]
    border_frame.config(bg=random.choice(colors))
    window.after(300, animate_border)

animate_border()

# Button Animation
def animate_button():
    colors = ["#FF1493", "#FFD700", "#00CED1", "#9400D3"]
    submit_button.config(bg=random.choice(colors))
    window.after(600, animate_button)

animate_button()

window.mainloop()
