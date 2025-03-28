import os
import shutil
import random


PERCENTAGE_TO_MOVE = 0.2

# Paths to your folders
images_folder = "data/train/images"  # Folder containing images
labels_folder = "data/train/labels"  # Folder containing labels (text files)
destination_folder = "data/val"  # Folder where 20% of data will go

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# List all image files (assuming they are all .jpg files, adjust the extension if necessary)
image_files = [f for f in os.listdir(images_folder)]

# Create a list of tuples containing image and label filenames
image_label_pairs = []
for img_file in image_files:
    label_file = os.path.splitext(img_file)[0] + ".txt"
    if label_file in os.listdir(
        labels_folder
    ):  # Ensure corresponding label file exists
        image_label_pairs.append((img_file, label_file))

# Calculate % of the total files
num_files_to_move = int(len(image_label_pairs) * PERCENTAGE_TO_MOVE)

# Randomly select 20% of the files
files_to_move = random.sample(image_label_pairs, num_files_to_move)

# Move the selected image and label files to the destination folder
for img_file, label_file in files_to_move:
    # Full paths
    img_src = os.path.join(images_folder, img_file)
    label_src = os.path.join(labels_folder, label_file)

    # Destination paths
    img_dst = os.path.join(destination_folder, "images", img_file)
    label_dst = os.path.join(destination_folder, "labels", label_file)

    # Move the image and label files
    shutil.move(img_src, img_dst)
    shutil.move(label_src, label_dst)

print(
    f"Successfully moved {num_files_to_move} image-label pairs to {destination_folder}"
)
