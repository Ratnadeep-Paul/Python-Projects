# Ooh Solder!! Preetify My Folder
# Input = Path, Dictionary, Format
# Make All File Preetiyer

# Import Section
import os

# User Input Section
path = input("Enter The Path Of The Folder\n:-- ")
os.chdir(path)
default_name = input("Enter A Default Name For All Files\n:-- ")

photo_count = 1
folder_item = os.listdir(path)
for item in folder_item:
    item_format_photo = item.endswith(".jpg")
    item_format_photo2 = item.endswith(".png")
    item_format_photo3 = item.endswith(".jpeg")

    if item_format_photo == True or item_format_photo2==True or item_format_photo3==True:
        if item_format_photo == True or item_format_photo3==True:
            new_name = f"{default_name}{photo_count}.jpg"
        elif item_format_photo2==True:
            new_name = f"{default_name}{photo_count}.png"
        elif item.endswith(".raw")==True:
            new_name = f"{default_name}{photo_count}.raw"
        elif item.endswith(".gif")==True:
            new_name = f"{default_name}{photo_count}.gif"
        os.rename(item, new_name)
        photo_count= photo_count+1
    else:
        print("This is i don' know")

print("Done!!!")