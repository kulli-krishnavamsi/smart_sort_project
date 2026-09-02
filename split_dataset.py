import os
import shutil
import random

source_folder = "datasets/Fruit And Vegetable Diseases Dataset"
train_folder = "dataset/train"
val_folder = "dataset/validation"

split_ratio = 0.7  
<<<<<<< HEAD
=======

>>>>>>> c030f53de01d33ec72498363afc1ad8e30dd6703

os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

for class_name in os.listdir(source_folder):
    class_path = os.path.join(source_folder, class_name)
    if os.path.isdir(class_path):
        images = os.listdir(class_path)
        random.shuffle(images)

        split_point = int(len(images) * split_ratio)
        train_images = images[:split_point]
        val_images = images[split_point:]

        train_class_dir = os.path.join(train_folder, class_name)
        val_class_dir = os.path.join(val_folder, class_name)

        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(val_class_dir, exist_ok=True)

        for img in train_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(train_class_dir, img)
            shutil.copyfile(src, dst)

        for img in val_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(val_class_dir, img)
            shutil.copyfile(src, dst)

print("✅ Dataset split into train and validation folders successfully!")
