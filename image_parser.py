import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


path_dir = 'images'
'''
file_list = os.listdir(path_dir)

for file in file_list:
    folder = 'images/'+file[:file.rfind('_')]
    createFolder(folder)
    print(shutil.move('images/'+file,folder))
'''
fold_list = os.listdir(path_dir+"/val")

for fold in fold_list:
    file_list = os.listdir(path_dir+"/val/"+fold)
    cnt=0
    for file in file_list:
        if cnt > 20:
            break
        createFolder('images/train/'+fold)
        shutil.move('images/val/'+fold+"/"+file,'images/train/'+fold)
        cnt+=1
'''
fold_list = os.listdir(path_dir)
for fold in fold_list:
    file_list = os.listdir(path_dir+"/"+fold)
    cnt=0
    for file in file_list:
        shutil.move('images/'+fold+"/"+file,'images/'+file)
        cnt+=1
'''