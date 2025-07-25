import os
import shutil
import random

# === CONFIG ===
dataset_dir = "Dataset" # Original dataset folder (contains subfolders for each food item)
output_dir = "gameplay_data" # Where train/val folders will be created
split_ratio = 0.8 # 80% train, 20% val
seed = 42 # For reproducibility

# === SETUP ===
random.seed(seed)
train_dir = os.path.join(output_dir, "train")
val_dir = os.path.join(output_dir, "val")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# === MAIN LOGIC ===
for food_class in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, food_class)
    
    if not os.path.isdir(class_path):
        continue # Skip non-folder files
    
    # Create same subfolders in train & val
    os.makedirs(os.path.join(train_dir, food_class), exist_ok=True)
    os.makedirs(os.path.join(val_dir, food_class), exist_ok=True)
    
    # Get all images for this class
    images = os.listdir(class_path)
    images = [img for img in images if os.path.isfile(os.path.join(class_path, img))]
    
    # Shuffle and split
    random.shuffle(images)
    split_idx = int(len(images) * split_ratio)
    train_images = images[:split_idx]
    val_images = images[split_idx:]
    
    # Copy files to train
    for img in train_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(train_dir, food_class, img)
        shutil.copy2(src, dst)
    
    # Copy files to val
    for img in val_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(val_dir, food_class, img)
        shutil.copy2(src, dst)
    
    print(f"{food_class}: {len(train_images)} train, {len(val_images)} val")

print("\n Dataset split completed!")
print(f"Train folder: {train_dir}")
print(f"Val folder: {val_dir}")