import os
import matplotlib.pyplot as plt
import imghdr
import tkinter as tk
import tkinter.filedialog as filedialog

def show_name_and_author():
    print("=" * 80)
    print("Branko Image Renaming Tool".center(80))
    print("by Luka Ernestini".center(80))
    print("=" * 80)

# Call the show_name_and_author function at the beginning of the script
show_name_and_author()

# Open a dialog to select a folder with the pictures
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory()

# Get a list of all the file paths for the images in the current directory
image_paths = []
for file in os.listdir(folder_path):
    # Check if the file is an image
    if imghdr.what(os.path.join(folder_path, file)):
        image_paths.append(os.path.join(folder_path, file))

# Open a separate window to display the images
plt.ion()

# Counter for showing progress
count = 1
# Iterate through the list of file paths
for image_path in image_paths:
    # Open the image and display it in the separate window
    image = plt.imread(image_path)
    plt.imshow(image)
    plt.show(block=False)

    # Get current file name without extension
    current_file_name = image_path.split('\\')
    current_file_name = current_file_name[len(current_file_name)-1]
    current_file_name = current_file_name.split('.', 1)[0]
    # Print position in folder and file name
    print(f'[{count}/{len(image_paths)}]: {current_file_name}')
    count += 1
    # Loop until unique name
    while True:
        # Prompt the user for a name for the file
        file_name = input("Enter a name for the file: ")
                
        unique = True
        # Get a list of all the file paths for the images in the current directory
        for file in os.listdir(folder_path):
            # Check whether file with the same name already exists
            if file_name == file.split('.')[0]:
                unique = False
        if unique:
            break
        print('!!! The file name was not unique, choose another one')

    # Clear the image from the window
    plt.clf()

    # Rename the file with the name provided by the user
    if file_name:
        os.rename(image_path, os.path.join(folder_path, file_name + "." + imghdr.what(image_path)))

# Close the separate window
plt.close()
