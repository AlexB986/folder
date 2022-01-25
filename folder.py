import os
import shutil
import re
root_src_dir = r'folder'
root_dst_dir = 'folder3'

for direct, papka, file in os.walk(root_src_dir):
    for files in file:
        dst_dir = direct.replace(root_src_dir,root_dst_dir,1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        cor = re.compile(r'pdf|jpg$')
        cor_file_1 = bool(cor.findall(files))
        if cor_file_1 != False:
            cor_file_1 =  files
            src_file = os.path.join(direct,cor_file_1)
            dst_file = os.path.join(dst_dir,cor_file_1)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copyfile(src_file,dst_file)