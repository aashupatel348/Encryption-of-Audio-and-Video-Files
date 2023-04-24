import os
import tkinter.filedialog

file_path = tkinter.filedialog.askopenfilename()
filename = str(file_path)

if filename.endswith(".mp4") or filename.endswith(".mkv"):
    command = f"ffmpeg -i {filename} -vcodec copy -acodec copy -encryption_scheme cenc-aes-ctr -encryption_key 76a6c65c5ea762046bd749a2e632ccbb -encryption_kid a7e61c373e219033c21091fa607bf3b8 SampleVideo_1280x720_1mb_encrypted.mp4"

elif filename.endswith(".mp3") or filename.endswith(".wav"):
    command = f"ffmpeg -i {filename} -codec:a copy -vcodec copy -encryption_scheme cbc -encryption_key 76a6c65c5ea762046bd749a2e632ccbb -encryption_iv a7e61c373e219033c21091fa607bf3b8 outputfile.m3u8"
    
else:
    print("Unsupported file format")
    exit()

os.system(command)
