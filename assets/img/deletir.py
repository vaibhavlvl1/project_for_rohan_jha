import os

def add_extension_to_files(extension=".webp"):
    for filename in os.listdir('.'):
        # Skip directories and already corrected files
        if os.path.isdir(filename) or '.' in filename:
            continue  

        new_name = filename + extension
        os.rename(filename, new_name)
        print(f'Renamed: {filename} -> {new_name}')

# Change the extension if needed (e.g., ".png" or ".jpg")
add_extension_to_files(".webp")