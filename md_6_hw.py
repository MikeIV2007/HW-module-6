"""Завдання
У багатьох на робочому столі є папка, яка називається якось на кшталт "Розібрати". Як правило, розібрати цю папку руки ніколи так і не доходять.

Ми з вами напишемо скрипт, який розбере цю папку. Зрештою ви зможете налаштувати цю програму під себе і вона виконуватиме індивідуальний сценарій, що відповідає вашим потребам. Для цього наш застосунок буде перевіряти розширення файлу (останні символи в імені файлу, як правило, після крапки) і, залежно від розширення, приймати рішення, до якої категорії віднести цей файл.

Скрипт приймає один аргумент під час запуску — це ім'я папки, в якій він буде здійснювати сортування. Припустимо, що файл з програмою називається sort.py, тоді, щоб відсортувати папку /user/Desktop/Мотлох, потрібно запустити скрипт командою python sort.py /user/Desktop/Мотлох

Для того щоб успішно впоратися з цим завданням, ви повинні винести логіку обробки папки в окрему функцію.
Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.
Скрипт повинен проходити по вказаній під час виклику папці та сортирувати всі файли за групами:

зображення ('JPEG', 'PNG', 'JPG', 'SVG');
відео файли ('AVI', 'MP4', 'MOV', 'MKV');
документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
музика ('MP3', 'OGG', 'WAV', 'AMR');
архіви ('ZIP', 'GZ', 'TAR');
невідомі розширення.
Ви можете розширити та доповнити цей список, якщо хочете.

В результатах роботи повинні бути:

Список файлів в кожній категорії (музика, відео, фото та ін.)
Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
Перелік всіх розширень, які скрипту невідомі.
Потім необхідно додати функції, які будуть відповідати за обробку кожного типу файлів.

Крім того, всі файли та папки потрібно перейменувати, видаливши із назви всі символи, що призводять до проблем. Для цього потрібно застосувати до імен файлів функцію normalize. Варто розуміти, що перейменувати файли потрібно так, щоб не змінити розширення файлів.

Функція normalize:

Здійснює транслітерацію кириличного алфавіту на латинський.
Замінює всі символи крім латинських літер, цифр на '_'.
Вимоги до функції normalize:

приймає на вхід рядок та повертає рядок;
здійснює транслітерацію кириличних символів на латиницю;
замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
транслітерація може не відповідати стандарту, але бути читабельною;
великі літери залишаються великими, а маленькі — маленькими після транслітерації.
Умови для обробки:
зображення переносимо до папки images
документи переносимо до папки documents
аудіо файли переносимо до audio
відео файли до video
архіви розпаковуються та їх вміст переноситься до папки archives

Критерії приймання завдання
всі файли та папки перейменовуються за допомогою функції normalize.
розширення файлів не змінюється після перейменування.
порожні папки видаляються
скрипт ігнорує папки archives, video, audio, documents, images;
розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів, але без розширення в кінці;
файли, розширення яких невідомі, залишаються без зміни.
"""
import os
import sys

"""first vertion"""
# import sys
# def sort_folder(path):
#     with open (path, 'r') as text:
#         print(text.readlines())
#         images = None # 'JPEG', 'PNG', 'JPG', 'SVG'
#         video = None #'AVI', 'MP4', 'MOV', 'MKV'
#         documents = None # 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'
#         music = None # 'MP3', 'OGG', 'WAV', 'AMR'
#         archives = None # 'ZIP', 'GZ', 'TAR'
#         Unknown = None
# return

"""Second version"""
images = []
images_tmp = ['.jpeg', '.png', '.jpg', '.svg']

video = [] 
video_tmp = ['.avi', '.mp4', '.mov', '.mkv', '.wmv']
    # documents = [] # 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'
    # music = [] # 'MP3', 'OGG', 'WAV', 'AMR'
    # archives = [] # 'ZIP', 'GZ', 'TAR'
    # Unknown = [] # other

"""normalize"""

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

# def simbol_to_replace(text):
#     for chr in text:
    
#         if ord(chr) in range(48,58):# (0-9)
#             continue
#         elif ord(chr) in range(65,91):#(A-Z)
#             continue
#         elif ord(chr) in range(97,123):#(a-z)
#             continue
#         else:
#             text = text.replace(chr, "_")
#     return text
    
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

def sort_folder(path, level = 1):

    #print ('level =', level, 'Content: ',os.listdir(path))
    for i in os.listdir(path):
        
        if os.path.isdir(path + '\\' + i):
            #print ('Going one level down', path + '\\' + i )
            sort_folder(path + '\\' + i, level + 1 )
            #print ("returning to ", path)

        else:
            file_name = os.path.basename(path + '\\' + i)
            file_extension = list (os.path.splitext(file_name))
            #print (file_name, file_extension, type(file_extension), file_extension[1], type(file_extension[1]))
            for ext in images_tmp:
                #print (f'{file_name} *** {file_extension[1]}')
               
                if file_extension[1] == ext:
                    file_extension[0] = normalize(file_extension[0])
                    #print (file_name, file_extension, type(file_extension), file_extension[1], type(file_extension[1]))
                    file_name = file_extension[0] + file_extension[1]
                    images.append(file_name)
           
            for ext in video_tmp:
                #print (f'{file_name} *** {file_extension[1]}')
               
                #print (images)
                if file_extension[1] == ext:
                    file_name
                    video.append(file_name)            
                
                    
                
                    #images_in_level.append (file_name)
            # images.extend(images_in_level)
    
    return images, video 



    
"""main method to start script"""
# path_input = sys.argv  # function gets arguments enered during script start
# #print (path_input)
# path = path_input[1]
# # print(path1)
# sort_folder(path)

"""test 1"""

path = 'D:\\VSCode_projects\\Unsorted_hw6_normalize_test'
sort_folder(path)
print ('\nImages = ',images, '\n','\nVideo = ',video)

"""test 2"""

# def main():
#     path = 'D:\\VSCode_projects\\Unsorted_hw6'
#     return sort_folder(path)

# if __name__ == 'main':
#     main()


