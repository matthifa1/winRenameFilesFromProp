import os
from win32com.client import Dispatch #pip install pywin32

user_input = input("Enter path to the files:")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
if False == os.path.exists(user_input):
    quit()

pathToMusic = user_input
shell = Dispatch("Shell.Application")
rename_array = {}
ns = shell.NameSpace(pathToMusic)
counter = 0
for i in ns.Items():
    # 2.Variable 0: name 1: size 2: type 3: data&Time 4: attributes etc.
    # schlecht dokumentiert und abhängig vom OS -> 21: Name
    newName = ns.GetDetailsOf(i,21)
    rename_array[counter] = [str(i), newName]
    counter += 1

print("The following file names will be renamed:")    
for i in rename_array:
    songNames = rename_array[i]
    #print(str(songNames[0]))
    print(songNames[0] + ' -> ' + songNames[1]+'.mp3')
    #os.rename(os.path.join(pathToMusic, songNames[0]), os.path.join(pathToMusic, songNames[1]+'.mp3'))

user_input = input("Do you want to rename all files? (y/n)")

if ('n'==user_input):
    print("No files renamed")
    quit()

for i in rename_array:
    songNames = rename_array[i]
    os.rename(os.path.join(pathToMusic, songNames[0]), os.path.join(pathToMusic, songNames[1]+'.mp3'))
