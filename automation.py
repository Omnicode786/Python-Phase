import os
import shutil




def changedir(directory):
    filestobechanges = {
        "Videos": [".mp4"], 
        "Songs":".mp3",
        "TextFiles": [".txt"],
          "Images":[".png", ".jpeg", ".jpg"], 
        "Zip files":[".rar",".7zip", ".zip"],
        "PDF and Documents": [".pdf", ".docx"]
    }
    if not os.path.exists(directory):
        print("The path was not found")
        return 1
    for folder in filestobechanges:
        folderpath = os.path.join(directory, folder)
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
    
    for file in os.listdir(directory):
        filekipath = os.path.join(directory,file)
        if os.path.isdir(filekipath):
            continue
        _, extension = os.path.splitext(file)
        for folder, extensions in filestobechanges.items():
            if extension.lower() in extensions:
                destination = os.path.join(directory,folder)
                shutil.move(filekipath, destination)
                print(f"{file} moved to {folder}")
                break
    print("Succesfully done meri jan ke tote")
def reverse_changedir(directory):
    filestobechanges = {
        "Videos": [".mp4"], 
        "Songs": [".mp3"],
        "TextFiles": [".txt"],
        "Images": [".png", ".jpeg", ".jpg"], 
        "Zip files": [".rar", ".7zip", ".zip"]
    }

    if not os.path.exists(directory):
        print("The path was not found")
        return 1

    # Iterate through folders and move files back to root directory
    for folder, extensions in filestobechanges.items():
        folderpath = os.path.join(directory, folder)
        if os.path.exists(folderpath):
            for file in os.listdir(folderpath):
                file_path = os.path.join(folderpath, file)
                _, extension = os.path.splitext(file)
                if extension.lower() in extensions:
                    destination = os.path.join(directory, file)
                    shutil.move(file_path, destination)
                    print(f"{file} moved back to the root directory")
            # Optionally, remove the folder after moving the files back
            os.rmdir(folderpath)
    print("Reverse operation completed successfully.")

changedir(r"C:\Users\lkj\OneDrive\Desktop")
# reverse_changedir(r"C:\Users\lkj\OneDrive\Desktop")
