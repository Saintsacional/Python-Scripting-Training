import os
import shutil
import argparse

def organize_files(directory):
    # Define file type categories
    file_types = {
        'Images-Organized': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents-Organized': ['.pdf', '.docx', '.txt'],
        'Videos-Organized': ['.mp4', '.avi', '.mkv'],
        'Audios-Organized': ['.mp3', '.wav'],
        'Others-Organized': []
    }

    # Go through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()  # Get file extension

            # Check which category the file belongs to
            category = 'others'  # Default category
            for key, extensions in file_types.items():
                if file_extension in extensions:
                    category = key
                    break

            # Create a folder for the category if it doesn't exist
            category_folder = os.path.join(directory, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            # Move the file to the corresponding folder
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"Moved {filename} to {category_folder}")

if __name__ == "__main__":
    # Set up argparse to accept the directory as an argument
    parser = argparse.ArgumentParser(description="Organize files in a directory by type.")
    parser.add_argument('directory', help="Path to the directory to organize.")
    args = parser.parse_args()

    # Call the organize_files function with the provided directory
    organize_files(args.directory)
    print("Done")
