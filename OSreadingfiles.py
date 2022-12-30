import os
import shutil
import send2trash

# os.getcwd())
# os.listdir('/root/Desktop')
# shutil.move('file.txt', 'C:\\Users\\Machine')		#moves a file to another destination
# os.unlink('path') 					#deletes a file at the path you proved
# os.rmdir('path')						#deletes a folder (folder must be empty) at the path you'r provide
# shutil.rmtree('path')					#this is the most dangerous, as it will remove all files and folders contained in the path.
# send2trash.send2trash('file.txt')			#sending the file to the trash

for folder, sub_folder, files in os.walk('C:\\Users\\legion\\Desktop\\hello'):

    print(f'Current folder {folder}\n')
    print('The subfolders are: ')

    for sub_fold in sub_folder:
        print(sub_fold)

    print('The files are: ')

    for f in files:
        print(f)