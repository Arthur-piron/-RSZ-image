import os
import easygui
from PIL import Image

print("WELCOME TO RESIZE IMAGE by Artcrus")
print("You can specify the absolute path for your directory if they aren't in your current directory.")

# Sélection des dossiers
source_dir = easygui.diropenbox(title="Select the Source Directory")
target_dir = easygui.diropenbox(title="Select the Target Directory")

# Dimensions exactes à prélever
x = int(input("Crop width (pixels): "))
y = int(input("Crop height (pixels): "))

os.makedirs(target_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.lower().endswith(".jpg"):
        filepath = os.path.join(source_dir, filename)
        with Image.open(filepath) as img:
            img = img.convert("RGB")

            # Vérifie que l’image est assez grande
            if img.width < x or img.height < y:
                print(f"[SKIPPED]: {filename} is smaller than the requested size ({x}x{y})")
                continue

            # Coordonnées pour crop centré
            left = (img.width - x) // 2
            top = (img.height - y) // 2
            right = left + x
            bottom = top + y

            cropped = img.crop((left, top, right, bottom))

            output_path = os.path.join(target_dir, filename)
            cropped.save(output_path)

            print("[DONE]:", filename, "has been cropped (center zoom)")