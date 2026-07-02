from rembg import remove
import easygui
from PIL import Image


inputpath = easygui.fileopenbox(title = 'select image')
outputimage = easygui.filesavebox(title = 'save here')

input = Image.open(inputpath)
output = remove(input)

output.save(outputimage)
print("done")