from os import walk
from shutil import move, rmtree
import zipfile

def unpack_zips_from_zip_folder(foldername="./zip"):
    zips = files_list_from_folder(foldername)

    counter = 0

    print('ZIPs left: ', end='')
    for zip in zips:
        print('[ ]', end='')
    print('\n___________', end='')

    # each archive
    for zip in sorted(zips):
        with zipfile.ZipFile(foldername + '/' + zip, 'r') as zip_ref:
            zip_ref.extractall('./temp')
        # unziped to ./temp
        temp_files = files_list_from_folder('./temp')
        # now move and rename every file in temp folder to images with index [counter] name

        for file in sorted(temp_files):
            file_extension = file.split('.')[-1]
            move('temp/' + file, 'images/' + str(counter) + '.' + file_extension)
            counter += 1

        print('[✓]', end='')
    print('\nDone. Check /images folder')

def duckling():
    print(open('.system_prop', 'r').read(), end='\n')

def files_list_from_folder(foldername="./zip"):
    files = []
    for dirpath, dirnames, filenames in walk(foldername):
        files.extend(filenames)    
        break
    return files

if __name__ == "__main__": 
    duckling()
    unpack_zips_from_zip_folder()