import os
import re

# paths
p_download = "/home/renato/Downloads/"
p_docs = "/home/renato/Downloads/docs/"
p_imagens = "/home/renato/Downloads/imagens/"
p_zipped = "/home/renato/Downloads/zipped/"

# tipos de arquivos
docs = ['.pdf', '.txt', '.doc', '.docx', '.odt', '.xls', '.ppt', '.pptx', '.ps', '.csv']
imagens = ['.jpg','.jpeg','.gif','.tiff','.webp','.bmp','.png','.ico','.svg']
zipped = ['.zip','.rar','.gz','.tar','.cab','.arj','.ace']

def get_type(f):
    return f[f.rfind('.'): ]

def mv(path, f):
    # renomeia arquivo caso tenha espaço no nome
    if ' ' in f:
        new_name = re.sub(' ','-', f)
        old_file = os.path.join(p_download, f)
        new_file = os.path.join(p_download, new_name)
        os.rename(old_file, new_file)
        f = new_name

    os.system(f'mv {p_download}{f} {path}')


while True:
    ls = os.listdir(p_download)
    for f in ls:
        tp = get_type(f)
        if tp in docs:
            mv(p_docs, f)
        elif tp in imagens:
            mv(p_imagens, f)
        elif tp in zipped:
            mv(p_zipped, f)
        else:
            continue
       
