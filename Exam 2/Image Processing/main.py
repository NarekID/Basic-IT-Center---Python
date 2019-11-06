from os import listdir, path
from random import randint as rnd
from time import sleep as slp

import pilgram
import re
from PIL import Image, ImageOps


def input_number(message):
    while 1:
        try:
            i = int(input(message))
            return i
        except ValueError:
            print("Enter a number!")


print("\n\n=====> Python Image Processing <======\n\n")

while 1:
    print("To start use, put your image to \'Original Images\' folder")
    if len(listdir("Original Images")) > 1:
        break
    slp(5)
format_jpg = ".jpg$"
image_name = input("Enter image \'name.format\': ")
while not path.isfile("Original Images/" + image_name) or len(re.findall(format_jpg, image_name)) == 0:
    image_name = input("Wrong! Try again! Enter image name.format: ")
image = Image.open("Original Images/" + image_name, "r")
width, height = image.size
print("Successful! File ", image_name, " is opened! Image width =", width, "px, height =", height, "px.")
change_count = 0
while 1:
    print("Select an action")
    print("0. Save & close")
    print("1. Apply filter")
    print("2. Crop")
    print("3. Resize")
    print("4. Flip")
    print("5. Rotate")
    print("6. Show current image")
    action = -1
    while action < 0 or action > 6:
        action = input_number("Your choice: ")
    print("\n" * 30)
    if action == 0:
        if change_count == 0:
            print("Closing program. Have a nice day!")
            break
        else:
            print("Save changes?")
            print("0. No")
            print("1. Yes")
            save_changes = -1
            while save_changes != 0 and save_changes != 1:
                save_changes = input_number("Your choice: ")
            if save_changes == 0:
                print("Closing program. Have a nice day!")
                break
            elif save_changes == 1:
                quality = input_number("Enter quality (1-95): ")
                if quality < 1:
                    quality = 1
                elif quality > 95:
                    quality = 95
                image.save("Edited Images/" + image_name, quality=quality)
                print("Image saved! Find here \'Edited Images/" + image_name)
                print("Closing program. Have a nice day!")
                break
    elif action == 1:
        print("Select filter")
        print("0. Cancel")
        print("1. Black & White")
        print("2. Negative")
        print("3. Random Instagram filter")
        filter_action = -1
        while filter_action < 0 or filter_action > 3:
            filter_action = input_number("Your choice: ")
        if filter_action == 0:
            print("Canceled!")
            slp(1)
            print("\n" * 30)
            continue
        elif filter_action == 1:
            print("Black & White selected")
            image = image.convert("L")
        elif filter_action == 2:
            print("Negative selected")
            image = ImageOps.invert(image)
        elif filter_action == 3:
            temp0 = rnd(1, 5)
            if temp0 == 1:
                print("Brannan filter selected.")
                image = pilgram.brannan(image)
            elif temp0 == 2:
                print("Hudson filter selected")
                image = pilgram.hudson(image)
            elif temp0 == 3:
                print("Valencia filter selected")
                image = pilgram.valencia(image)
            elif temp0 == 4:
                print("Reyes filter selected")
                image = pilgram.reyes(image)
            elif temp0 == 5:
                print("Clarendon filter selected")
                image = pilgram.clarendon(image)
        change_count = 1
    elif action == 2:
        print("Crop")
        print("0. Cancel")
        print("1. Start")
        crop_action = -1
        while crop_action != 0 and crop_action != 1:
            crop_action = input_number("Your choice: ")
        if crop_action == 0:
            print("Canceled!")
            slp(1)
            print("\n" * 30)
            continue
        elif crop_action == 1:
            startX = -1
            while startX < 0 or startX == width:
                startX = input_number("Enter start X postition: ")
            startY = -1
            while startY < 0 or startY == height:
                startY = input_number("Enter start Y postition: ")
            endX = width + 1
            while endX > width or endX <= startX:
                endX = input_number("Enter end X postition: ")
            endY = height + 1
            while endY > height or endY <= startY:
                endY = input_number("Enter end Y postition: ")
            area = (startX, startY, endX, endY)
            image = image.crop(area)
            width, height = image.size
        change_count = 1
    elif action == 3:
        print("Resize")
        print("0. Cancel")
        print("1. Start")
        resize_action = -1
        while resize_action != 0 and resize_action != 1:
            resize_action = input_number("Your choice: ")
        if resize_action == 0:
            print("Canceled!")
            slp(1)
            print("\n" * 30)
            continue
        elif resize_action == 1:
            print("Original size - width", width, "px, height", height, "px.")
            new_width = -1
            new_height = -1
            while new_width <= 0:
                new_width = input_number("Input new width: ")
            while new_height <= 0:
                new_height = input_number("Input new height: ")
            new_size = (new_width, new_height)
            image = image.resize(new_size, Image.LANCZOS)  # Same as ANTIALIAS
            width, height = image.size
        change_count = 1
    elif action == 4:
        print("Flip")
        print("0. Cancel")
        print("1. Vertical")
        print("2. Horizontal")
        flip_action = -1
        while flip_action < 0 or flip_action > 2:
            flip_action = input_number("Your choice: ")
        if flip_action == 0:
            print("Canceled!")
            slp(1)
            print("\n" * 30)
            continue
        elif flip_action == 1:
            image = ImageOps.flip(image)
        elif flip_action == 2:
            image = ImageOps.mirror(image)
        change_count = 1
    elif action == 5:
        print("Rotate")
        print("0. Cancel")
        print("1. Rotate right 90°")
        print("2. Rotate left 90°")
        print("3. Rotate 180°")
        rotate_action = -1
        while rotate_action < 0 or rotate_action > 3:
            rotate_action = input_number("Your choice: ")
        if rotate_action == 0:
            print("Canceled!")
            slp(1)
            print("\n" * 30)
            continue
        elif rotate_action == 1:
            image = image.rotate(270)
        elif rotate_action == 2:
            image = image.rotate(90)
        elif rotate_action == 3:
            image = image.rotate(180)
        change_count = 1
    elif action == 6:
        image.show()
    print("Success!")
    slp(2)
    print("\n" * 30)

image.close()