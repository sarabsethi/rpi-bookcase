import os
from PIL import Image
from inky.auto import auto
import argparse
from subprocess import call
import time 
import os
import random 

current_img_txt_f = '/home/pi/current_img.txt'
book_covers_dir = 'book_covers' 

# Get command line argument of whether to shutdown or not
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--shutdown', default=False, type=bool, help='Shutdown after changing picture')
args = parser.parse_args()
shutdown_after_change = args.shutdown

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

# Set up inky display and show new image
print('Setting image to {}'.format(new_book_cover_f))
inky_display = auto(ask_user=False, verbose=True)
img = Image.open(os.path.join(book_covers_dir, new_book_cover_f))
img = img.transpose(Image.ROTATE_90)
inky_display.set_image(img)
inky_display.show()

# Write the currently showing image file to file
with open(current_img_txt_f, 'w') as f:
    f.write(new_book_cover_f)

# If asked for in args, shut down device
if shutdown_after_change:
    time.sleep(60)
    call("sudo halt", shell=True)