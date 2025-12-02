from PIL import Image

# Parametri
input_path = "sticker_art/ponyo.png"
output_path = "pixelart.png"
block_size = 50  # NxN pixel

# Apri immagine
img = Image.open(input_path)
img = img.convert('RGB')  # assicurati sia RGB

# Calcola dimensione nuova immagine ridotta
width, height = img.size
new_width = width // block_size
new_height = height // block_size

# Ridimensiona a dimensione ridotta usando il filtro BOX (media dei pixel)
small_img = img.resize((new_width, new_height), resample=Image.BOX)

# Ridimensiona di nuovo all'originale moltiplicando per block_size
pixel_art_img = small_img.resize((new_width*block_size, new_height*block_size), Image.NEAREST)

# Salva
pixel_art_img.save(output_path)
print("Pixel art creata!")