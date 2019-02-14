import re
import os
import sys

directory = '.'
files = os.listdir(directory)


def print_files_on_dir():
    n = 0   
    print ('')
    print ('')
    print ('===List of files===')
    print ('')
    print ('')
    while n < len(files):
        name_of_file = files[n]
        result_string = "[" + str(n) + "]" + " - " + name_of_file
        print (result_string)
        n += 1
    print ('')
    print ('')
    print ('===================')
    print ('')
    print ('Select FILE with tests. Enter the number:')

def find_conditions(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    
    n = 0
    speech_list = []
    equal_speech = False
    
    for line in f:
        result = re.findall(r'("text":.".*"|"speech":.".*")',line)
        if result:
            while n < len(speech_list):
                if speech_list[n] == result:
                    equal_speech = True
                n += 1
            if equal_speech == False:
                speech_list.append(result)
            else:
                equal_speech = False
    make_speechs_file(file_path, speech_list)
    
def make_speechs_file(file_path, speech_list): 
    newfile = re.sub(r'\..*', '', file_path) 
    newfile = newfile + "_speech.txt"
    if os.path.exists(newfile):
        os.remove(newfile)
    f = open(newfile, "w")
    for speech in speech_list:
        format_speech = re.sub(r'("text":."|"speech":."|\[\'|\"\'\])', '', str(speech)) 
        format_speech = format_speech + "\n"
        f.write(format_speech)
    f.close
    
print_files_on_dir() #files in dir
find_conditions(str(files[int(input())]))
