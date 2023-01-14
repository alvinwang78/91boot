# 导入模块

import os
import sys

from docx import Document

path = sys.argv[1]

old_word = sys.argv[2] + '-'
new_word = sys.argv[3] + '-'

#取路径下的文件名，生成列表
for root, dirs, files in os.walk(path):
    for old_name in files:

        ext = os.path.splitext(old_name)[-1]
        

        if (ext == '.docx'):
            print(old_word)

            if old_name.startswith(old_word):

                print(old_name)

                new_name = old_name.replace(old_word, new_word)
                os.rename(os.path.join(root,old_name),os.path.join(root,new_name))
                    
                #print (old_name,"has been renamed successfully! New name is: ",new_name) 





