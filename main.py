from lib2to3.pgen2.token import LEFTSHIFTEQUAL
import pathlib
import os

ROOT_DIR='C:\photos'

path=pathlib.Path(ROOT_DIR)

print(path,type(path))

print(os.path.abspath(ROOT_DIR))

entries = path.iterdir()
entries = sorted(entries, key=lambda entry: entry.is_file())
entries_count = len(entries)
print(entries_count)
print(os.listdir(path))
print(os.scandir(path))
ltf=[]
# print(os.listdir(path))
for d,f,fl in os.walk(ROOT_DIR):
    if fl is not None:
        for i in fl:
            print(type(os.path.join(d,i)))
            ltf.append(os.path.join(d,i))
print(len(ltf))
import shutil

# for flname in ltf:
#     shutil.copy(flname,'C:\photos\Dest')
pfl=[]
for f in path.glob('**/*'):
    # print(type(f))
    if f.is_file():
        pfl.append(f)

print(len(pfl))
# print(pfl)