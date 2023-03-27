import os
from PIL import Image
from inky.auto import auto
import os
import random 

current_img_txt_f = '/home/pi/current_img.txt'

book_covers_dir = 'book-covers-full-res' 

screen_pix_h = 800
screen_pix_w = 480

# Get last shown image
current_img_f = ''
if os.path.exists(current_img_txt_f):
    with open(current_img_txt_f) as f:
        current_img_f = f.readlines()[0]
        print('Current image showing is: {}'.format(current_img_f))

# Get list of all book covers and randomly choose a new one
all_book_covers = os.listdir(book_covers_dir)
all_book_covers = [b for b in all_book_covers if b != current_img_f]
print('Choosing randomly from: {}'.format(all_book_covers))
new_book_cover_f = random.choice(all_book_covers)

# Load full size image and downsize to thumbnail that will fit in screen
img = Image.open(os.path.join(book_covers_dir, new_book_cover_f))
desired_sz = screen_pix_w, screen_pix_h
img.thumbnail(desired_sz, Image.LANCZOS)

# Copy thumbnail to image with correct screen dimensions to add border
new_size = (screen_pix_w, screen_pix_h)
final_img = Image.new("RGB", new_size, "White")  
box = tuple((n - o) // 2 for n, o in zip(new_size, img.size))
final_img.paste(img, box)

# Set up inky display and show new image
print('Setting image to {}'.format(new_book_cover_f))
inky_display = auto(ask_user=False, verbose=True)
final_img = final_img.transpose(Image.ROTATE_90)
inky_display.set_image(final_img)
inky_display.show()

# Write the currently showing image file to file
with open(current_img_txt_f, 'w') as f:
    f.write(new_book_cover_f)
