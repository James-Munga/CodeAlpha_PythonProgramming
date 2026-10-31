
import os
import shutil

# Define the source and destination folders
source_folder = r"D:\ArdhiLens\Images"
destination_folder = r"D:\ArdhiLens\Organized_Images"

print("====================================")
print("       IMAGE FILE ORGANIZER")
print("====================================")

# Check whether the source folder exists
if not os.path.exists(source_folder):

    print("Source folder does not exist!")
    print("Please create a folder named 'images' first.")

else:

    # Create destination folder if it does not exist
    os.makedirs(destination_folder, exist_ok=True)

    # Count moved files
    moved_files = 0

    # Read files from the source folder
    for filename in os.listdir(source_folder):

        # Check whether the file is a JPG image
        if filename.lower().endswith(".jpg"):

            source_path = os.path.join(source_folder, filename)

            destination_path = os.path.join(
                destination_folder, filename
            )

            # Avoid overwriting an existing file
            if os.path.exists(destination_path):
                print("Skipped (already exists):", filename)
                continue

            # Move the image
            shutil.move(source_path, destination_path)

            print("Moved:", filename)

            moved_files += 1

    # Display summary
    print("\n====================================")
    print("       AUTOMATION SUMMARY")
    print("====================================")

    print("Total images moved:", moved_files)

    print("Destination folder:", destination_folder)

    print("\nTask completed successfully!")
