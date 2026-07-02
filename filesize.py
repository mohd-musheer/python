import os
import easygui

inputpath = easygui.fileopenbox(title = 'select image')

path = inputpath

if path :
    sizeoffile = os.path.getsize(path)
    print("file size in BYTES is : " , sizeoffile," Bytes")
    print("file size in kb is : " , sizeoffile/1024," KB")
    print("file size in mb is : " , sizeoffile/1024/1024," MB")
else:
    print("file not selected ")