import os
import easygui
from PIL import Image

print("WELCOME TO RESIZE IMAGE by Artcrus")

print("You can specify the absolute path for your directory if they aren't in your current directory.")

# Utiliser easygui pour sélectionner le dossier source et cible
source_dir = easygui.diropenbox(title="Select the Source Directory")
target_dir = easygui.diropenbox(title="Select the Target Directory")

# Demander les dimensions
x = int(input("New size x: "))
y = int(input("New size y: "))
new_dimensions = (x, y)
background_color = input("Choose the color of the background you are going to add (in English): ")

os.makedirs(target_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.lower().endswith(".jpg"):
        filepath = os.path.join(source_dir, filename)
        with Image.open(filepath) as img:
            img_ratio = img.width / img.height
            target_ratio = x / y

            if img_ratio > target_ratio:
                new_width = x
                new_height = round(x / img_ratio)
            else:
                new_height = y
                new_width = round(y * img_ratio)

            img_resized = img.resize((new_width, new_height), Image.LANCZOS)

            background = Image.new("RGB", (x, y), color=background_color)
            offset = ((x - new_width) // 2, (y - new_height) // 2)
            background.paste(img_resized, offset)

            output_path = os.path.join(target_dir, filename)
            background.save(output_path)

            print("[DONE]:", filename, "has been successfully resized")
