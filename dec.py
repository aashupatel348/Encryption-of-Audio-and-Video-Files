
import os
import tkinter.filedialog

file_path = tkinter.filedialog.askopenfilename()
filename = str(file_path)

if filename.endswith(".mp4"):
    command = f"ffplay {filename} -decryption_key 76a6c65c5ea762046bd749a2e632ccbb"


elif filename.endswith(".m3u8"):
    command = f"ffmpeg -allowed_extensions ALL -i {filename} -codec:a copy -vcodec copy -encryption_scheme cbc -encryption_key 76a6c65c5ea762046bd749a2e632ccbb -encryption_iv a7e61c373e219033c21091fa607bf3b8 outputfile.mp3"

else:
    print("Unsupported file format")
    exit()

os.system(command)
