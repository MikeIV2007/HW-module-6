import os
import sys
import shutil
import zipfile


images = []
images_tmp = ['.jpeg', '.png', '.jpg', '.svg']

video = [] 
video_tmp = ['.avi', '.mp4', '.mov', '.mkv', '.wmv']

documents = []
documents_tmp =['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']

music = [] 
music_tmp =  ['.mp3', '.ogg', '.wav', '.amr']

archives = []
archives_tmp =  ['.zip', '.gz', '.tar']
unknown = []
all_extentions = set()

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(text):
    text = text.translate(TRANS)
    for chr in text:
        if ord(chr) in range(48,58):# (0-9)
            continue
        elif ord(chr) in range(65,91):#(A-Z)
            continue
        elif ord(chr) in range(97,123):#(a-z)
            continue
        else:
            text = text.replace(chr, "_")
    return text

def sort_folder(path):
    
    for i in os.listdir(path):
         
        if os.path.isdir(path + '\\' + i) == True:
            folder_name = normalize(i)
            os.rename(path + '\\' + i, path + '\\' + folder_name)
            sort_folder(path + '\\' + folder_name)


        if os.path.isfile(path + '\\' + i) == True:
            file_name = i
            file_extension = list (os.path.splitext(file_name))
            file_extension[0] = normalize(file_extension[0])
            file_name = file_extension[0] + file_extension[1]
            os.rename(path + '\\' + i, path + '\\' + file_name)
    
            for ext in images_tmp:
                if file_extension[1] == ext:
                    all_extentions.add(file_extension[1])
                    images.append(file_name)
                    shutil.move(path + '\\' + file_name, path_images + '\\' + file_name)

            for ext in video_tmp:
                
                if file_extension[1] == ext:
                    all_extentions.add(file_extension[1])
                    video.append(file_name)
                    shutil.move(path + '\\' + file_name, path_video + '\\' + file_name)
                                          
            for ext in documents_tmp:
                if file_extension[1] == ext:
                    all_extentions.add(file_extension[1])
                    documents.append(file_name)
                    shutil.move(path + '\\' + file_name, path_documents + '\\' + file_name)          

            for ext in music_tmp:
                if file_extension[1] == ext:
                    all_extentions.add(file_extension[1])
                    music.append(file_name)
                    shutil.move(path + '\\' + file_name, path_music + '\\' + file_name)

            for ext in archives_tmp:
                if file_extension[1] == ext:
                    all_extentions.add(file_extension[1])
                    archives.append(file_name)
                    shutil.move(path + '\\' + file_name, path_archives + '\\' + file_name)
                    
            if file_extension[1] not in images_tmp and file_extension[1] not in video_tmp and file_extension[1] not in documents_tmp and file_extension[1] not in music_tmp and file_extension[1] not in archives_tmp :
                    all_extentions.add(file_extension[1])
                    unknown.append(file_name)
                    shutil.move(path + '\\' + file_name, path_unknown + '\\' + file_name)
                
    return images, video, documents, music, unknown, all_extentions

def delete_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):

        for folder in dirs:
            folder_path = os.path.join(root, folder)
        
            if not os.listdir(folder_path):  # Check if folder is empty
                os.rmdir(folder_path)

def unzip_archivez(path_archves):

    for i in os.listdir(path_archives):
        file_extension = list (os.path.splitext(i))
        folder_name = file_extension[0]
    
        extraction_path = os.path.join(path_archives, folder_name)

        if not os.path.exists(extraction_path):
            os.makedirs(extraction_path)

        with zipfile.ZipFile(path_archives + '\\' + i, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)


path_input = sys.argv
path = path_input[1]

path_images = path + '\\' + 'images'
if not os.path.exists(path_images):
    os.makedirs(path_images)

path_video = path + '\\' + 'video'
if not os.path.exists(path_video):
    os.makedirs(path_video)

path_documents = path + '\\' + 'documents'
if not os.path.exists(path_documents):
    os.makedirs(path_documents)

path_music = path + '\\' + 'music'
if not os.path.exists(path_music):
    os.makedirs(path_music)

path_archives = path + '\\' + 'archives'
if not os.path.exists(path_archives):
    os.makedirs(path_archives)

path_unknown = path + '\\' + 'unknown'
if not os.path.exists(path_unknown):
    os.makedirs(path_unknown)

sort_folder(path)
delete_empty_folders(path)
all_extentions =list(all_extentions)
unzip_archivez(path_archives)
print ('\nImages = ',images, '\n',
       '\nVideo = ',video, '\n'
       '\nDocuments = ',documents, '\n'
       '\nMusic = ',music, '\n'
       '\nArchives = ',archives, '\n'
       '\nUnknown = ',unknown, '\n'
       '\nAll_exstensions = ',all_extentions)



