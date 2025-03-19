import random
from PIL import Image, ImageTk, ImageOps
import os
import tkinter as tk

# Initialize window
window = tk.Tk()
window.title("Alphabet Game")
window.geometry("900x850")

# Create gradient background using canvas
canvas = tk.Canvas(window, width=900, height=800)
canvas.pack(fill="both", expand=True)

def create_gradient():
    for i in range(1000):
        color = f"#{int(255 * (i / 1000)):02x}{int(120 + 135 * (i / 1000)):02x}FF"
        canvas.create_line(0, i, 1000, i, fill=color)

create_gradient()

# Alphabetical association
Pictionary = [
    "Apple", "Ball", "Cat", "Dog", "Elephant", "Fish", "Grapes",
    "Hat", "Ice", "Jellyfish", "King", "Lion", "Mango", "Nest", 
    "Peacock", "Queen", "Rabbit", "Sun", "Toy", "Umbrella", "Violin", 
    "Whale", "Xylophone", "Yak", "Zebra"
]

# Generate a random object
randIndex = random.randint(0, len(Pictionary) - 1)
selected_object = Pictionary[randIndex]
print(f"Selected Object (for debugging): {selected_object}")
guesses = 0

# Set the absolute image path
image_path = f"C:/Users/SNEHA/Desktop/python/Python-practice/project4/images/{randIndex + 1}.jpg"

# Verify if image exists
if not os.path.exists(image_path):
    print(f"Error: Image not found at path: {image_path}")
    exit()

# Load Image with colorful changing border
try:
    image = Image.open(image_path)
    image = image.resize((400, 400))
    photo = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error loading image: {e}")
    exit()

border_frame = tk.Label(window, bg="red")
border_frame_window = canvas.create_window(500, 350, window=border_frame, width=430, height=430)

image_label = tk.Label(window, image=photo, bg="#FFD1DC")
image_label_window = canvas.create_window(500, 350, window=image_label)

def animate_border():
    colors = ["#FF1493", "#FFD700", "#00CED1", "#9400D3", "#32CD32"]
    border_frame.config(bg=random.choice(colors))
    window.after(300, animate_border)

animate_border()

# UI Elements
label = tk.Label(window, text="Pictionary: Guess the object!", font=("Comic Sans MS", 24), bg="#FFD1DC", fg="#6A0572")
label_window = canvas.create_window(500, 80, window=label)

entry = tk.Entry(window, font=("Comic Sans MS", 18), bg="#FFF5BA", fg="#FF1493", justify="center")
entry_window = canvas.create_window(500, 600, window=entry)

result_label = tk.Label(window, text="", font=("Comic Sans MS", 18), fg="#00CED1")
result_label_window = canvas.create_window(500, 650, window=result_label)

# Check guess function
def check_guess():
    global guesses
    user_guess = entry.get().strip().capitalize()
    guesses += 1

    if user_guess == selected_object:
        result_label.config(text=f"🎉 Correct! You guessed it in {guesses} attempts! 🎉", fg="#32CD32")
    else:
        result_label.config(text="❌ Wrong guess! Try again.", fg="#FF4500")

# Submit button with animation
submit_button = tk.Button(window, text="Submit", command=check_guess, bg="#9400D3", fg="#FFFFFF", font=("Comic Sans MS", 18))
submit_button_window = canvas.create_window(500, 700, window=submit_button)

def animate_button():
    colors = ["#FF1493", "#FFD700", "#00CED1", "#9400D3"]
    current_color = random.choice(colors)
    submit_button.config(bg=current_color)
    window.after(700, animate_button)

animate_button()
window.mainloop()
