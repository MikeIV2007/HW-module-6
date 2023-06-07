import sys


path = ''

def get_main_path():

    path_input = sys.argv
    path = path_input[1]
    print ('path inner = ', path)

    return path

get_main_path()
print ('path global = ',path)

#Path to test: python test_01.py D:\\VSCode_projects\\Unsorted_hw6_main