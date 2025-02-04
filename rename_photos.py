import os

def rename_photos(directory):
    image_extensions = ['jpg', 'jpeg', 'png', 'gif']
    images = [f for f in os.listdir(directory) if any(f.lower().endswith(ext) for ext in image_extensions)]
    images.sort()  # Sort to ensure consistent naming

    for index, filename in enumerate(images, start=1):
        ext = filename.split('.')[-1]
        new_name = f"photo{index}.{ext}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

if __name__ == "__main__":
    photos_directory = "C:/Users/liam suorsa/programmerings filer/python/picture showcase/photos"
    rename_photos(photos_directory)
