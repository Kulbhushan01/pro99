import time
import os
import shutil

path = "C:/Users/Kulbh/OneDrive/Desktop/python"  
days = 30

seconds = days * 24 * 3600

if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            full_path = os.path.join(root, name)
            ctime = os.stat(full_path).st_ctime
            if time.time() - ctime > seconds:
                if os.path.isfile(full_path):
                    os.remove(full_path)
                    print(f"Deleted file: {full_path}")
                else:
                    shutil.rmtree(full_path)
                    print(f"Deleted folder: {full_path}")
else:
    print("Path not found.")
