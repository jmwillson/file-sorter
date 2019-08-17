import os
import os.path
from os import listdir

home_dir = os.environ['HOME']

default_path = home_dir + "/Downloads/"
pictures_path = home_dir + "/Pictures/"
videos_path = home_dir + "/Videos/"
txt_path = home_dir + "/Documents/"
aud_path = home_dir + "/Music/"

aud_formats = [".aac", ".aiff", ".m4a", ".mp3", ".wav", ".wma"]
img_formats = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
vid_formats = [".webm", ".avi", ".mov", ".qt", ".mpeg", ".mpg", ".mp2", ".mpe", ".mpv", ".mp4", ".flv",
                ".m4v", ".m2v", ".amv", ".mkv"]
txt_formats = [".txt", ".xml", ".json", ".pdf", ".rtf", ".docx", ".doc", ".ascii", ".log"]

formats = [aud_formats, img_formats, vid_formats, txt_formats]

def get_extension(file):
    ext = os.path.splitext(file)[1]
    return ext


def categorise_file(e, file):
    if e == "img":
        move_files(default_path + file, pictures_path + file)
    elif e == "vid":
        move_files(default_path + file, videos_path + file)
    elif e == "aud":
        move_files(default_path + file, aud_path + file)
    elif e == "txt":
        move_files(default_path + file, txt_path + file)

def sort_files(file, ext):
    print("Processing file: " + file)

    for format in formats:
        for f in format:
            if ext == f:
                print("File Type Found: " + f)
                if f in img_formats:
                    file_type = "img"
                    categorise_file(file_type, file)
                elif f in aud_formats:
                    file_type = "aud"
                    categorise_file(file_type, file)
                elif f in vid_formats:
                    file_type = "vid"
                    categorise_file(file_type, file)
                elif f in txt_formats:
                    file_type = "txt"
                    categorise_file(file_type, file)

def move_files(src, dst):
    print("Moving file " + src + " to " + dst)
    os.rename(src, dst)

def get_files(path):
    files = os.listdir(path)
    for f in files:
        file_ext = get_extension(f)
        sort_files(f, file_ext)

def main():
    get_files(default_path)

if '__main__' == __name__:
    main()


