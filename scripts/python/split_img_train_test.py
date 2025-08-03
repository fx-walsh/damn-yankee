import os
import shutil
import random

image_dir = "../damn-yankee-data/yolo/images"
label_dir = "../damn-yankee-data/yolo/labels"
output_dir = "../damn-yankee-data/yolo"

train_ratio = 0.8  # 80% train, 20% val
image_extensions = [".jpg", ".jpeg", ".png"]

# Create output folders
for split in ["train", "val"]:
    os.makedirs(os.path.join(output_dir, "images", split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "labels", split), exist_ok=True)

# Get list of image basenames (without extension)
image_files = [f for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in image_extensions]
base_names = [os.path.splitext(f)[0] for f in image_files]

# Shuffle and split
random.shuffle(base_names)
split_index = int(len(base_names) * train_ratio)
train_set = base_names[:split_index]
val_set = base_names[split_index:]

def copy_files(basenames, split):
    for base in basenames:
        # Copy image
        image_path = next((os.path.join(image_dir, base + ext)
                           for ext in image_extensions
                           if os.path.exists(os.path.join(image_dir, base + ext))), None)
        if image_path:
            shutil.copy(image_path, os.path.join(output_dir, "images", split))

        # Copy label
        label_path = os.path.join(label_dir, base + ".txt")
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_dir, "labels", split))
        else:
            print(f"⚠️  Warning: Label missing for {base}")

# Copy files to train/val
copy_files(train_set, "train")
copy_files(val_set, "val")

print(f"✅ Dataset split complete: {len(train_set)} training and {len(val_set)} validation samples.")
