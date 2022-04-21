from collections import defaultdict
import pathlib
import os
import shutil
from typing import Dict, List

#get the file names as dict
def get_file_names_by_pathlib(root_path:str)-> Dict[str,List[str]]:
    dir_files=defaultdict(list)
    base_path=pathlib.Path(root_path)
    root_dir=base_path.iterdir()
    for dir in root_dir:
        for file in dir.glob('**/*'):
            if file.is_file():
                dir_files[dir].append(file)
    # print(dict(dir_files))
    return dir_files

# get the files name by using os module
def get_file_names_by_oswalk(root_path:str)-> Dict[str,List[str]]:
    dir_files=defaultdict(list)
    base_folders=os.listdir(root_path)
    for folder in base_folders:

        for root,directory,files in os.walk(os.path.join(root_path,folder)):
            if files is not None:
                for file in files:
                    dir_files[os.path.join(root_path,folder)].append(os.path.join(root,file))
    # print(dir_files)
    return dir_files

#get just the list of all file name
def get_list_of_all_filenames(root_path:str)-> List[str]:
    file_names=[]
    for item in pathlib.Path(root_path).glob('**/*'):
        if item.is_file():
            file_names.append(item)
    print(file_names)
    return file_names


#split list
def split_list(whole_list,chunk_size):
    k,m=divmod(len(whole_list),chunk_size) #retuns quotient and reminder in tuple
    return (whole_list[i*k+min(i,m):(i+1)*k+min(i+1,m)] for i in range(chunk_size))


def copy_file_to_dest(file_list,dest='C:\photos\Dest'):
    for flname in file_list:
        try:
            shutil.copy(flname,dest)
        except shutil.SameFileError:
            pass

def copy_files(file_rec:defaultdict):
    print(file_rec)
    if isinstance(file_rec,defaultdict):
        print('it is a defaultdict')
        for base_folder,file_list in file_rec.items():
            print(f'copying files in {base_folder}')
            copy_file_to_dest(file_list)
    elif isinstance(file_rec,list):
        print('its a list')
        copy_file_to_dest(file_rec)



if __name__=='__main__':
    ROOT_DIR='C:\photos'
    # ROOT_DIR=r'C:\Users\Pratheek M S\Desktop\pinc'
    # file_records=get_file_names_by_pathlib(root_path=ROOT_DIR)
    # file_records=get_file_names_by_oswalk(root_path=ROOT_DIR)
    file_records=get_list_of_all_filenames(root_path=ROOT_DIR)

    copy_files(file_records)

    # import time
    # shutil.rmtree('C:\photos\Dest')
    # os.mkdir('C:\photos\Dest')
    # start=time.perf_counter()
    # print('normal copy started')
    # copy_file_to_dest(file_list=file_list_pl)
    # end=time.perf_counter()
    # print(f'total time normal={end-start}')
    # shutil.rmtree('C:\photos\Dest')
    # os.mkdir('C:\photos\Dest')
    # nl=list(split_list(file_list_pl,5))
    # import concurrent.futures as cf
    # start=time.perf_counter()
    # print('pool copy started')
    # with cf.ProcessPoolExecutor() as p_executor:
    #     res=p_executor.map(copy_file_to_dest,nl)
    # end=time.perf_counter()
    # print(f'total time pool={end-start}')
    # shutil.rmtree('C:\photos\Dest')
    # os.mkdir('C:\photos\Dest')
    # start=time.perf_counter()
    # print('thread copy started')
    # with cf.ThreadPoolExecutor() as t_executor:
    #     res=t_executor.map(copy_file_to_dest,nl)
    # end=time.perf_counter()
    # print(f'total time thread={end-start}')