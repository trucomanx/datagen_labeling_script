#!/usr/bin/python

import os
import sys

## Para cada image con varias personas: Divide en varias imagens con una persona por imagen.
## El resultado es colocado en 'output'.
## Si solo hay una persona se asume que es un paciente y se envia la directorio "paciente".
## Si hay mas de una persona en la imagen estas se envian a un directorio "incognita".

sys.path.append('/home/fernando/Proyectos/PÓS-GRADUAÇÂO/TESIS-DOUTORADO-2/PESQUISA/software/WorkingWithFiles/library');
import WorkingWithFiles as rnfunc

sys.path.append('/home/fernando/Proyectos/PÓS-GRADUAÇÂO/TESIS-DOUTORADO-2/PESQUISA/software/OpenpifpafTools/library');
import OpenpifpafAnnotations as opp
import OpenpifpafGetData as oppd


basedir='/mnt/boveda/DATASETs/PATIENT-IMAGES';

negative_list=[ os.path.join(basedir,"dataset_800/anger"),
                os.path.join(basedir,"dataset_800/disgust"),
                os.path.join(basedir,"dataset_800/fear"),
                os.path.join(basedir,"dataset_800/pain"),
                os.path.join(basedir,"dataset_800/sad"),
                os.path.join(basedir,"dataset_800/surprise-disgust")];
neutral_list =[ os.path.join(basedir,"dataset_800/neutro")]
positive_list=[ os.path.join(basedir,"dataset_800/happy"),
                os.path.join(basedir,"dataset_800/surprise-happy")];

lista1=rnfunc.get_all_files_in_dir_list(negative_list);
lista2=rnfunc.get_all_files_in_dir_list(neutral_list);
lista3=rnfunc.get_all_files_in_dir_list(positive_list);


output='output'; ## "patient_people"
path_paciente  = os.path.join(output,'paciente');
path_incognita = os.path.join(output,'incognita');
try: 
    os.mkdir(output) 
except: 
    pass
try: 
    os.mkdir(path_paciente) 
    os.mkdir(path_incognita) 
except: 
    pass

total=lista1+lista2+lista3

k=1;
j=1;
filename="filename";
for filepath in total:
    print(filepath)
    annotation,pil_im=opp.get_openpifpaf_annotation_from_imgpath(filepath);
    N=len(annotation);
    if(N>1):
        for annot in annotation:
            tupla=oppd.get_body_bounding_rectangle(annot.data, factor=1.4);
            if not((tupla[0]==0)and(tupla[1]==0)and(tupla[2]==0)and(tupla[3]==0)):
                tupla=oppd.get_valid_bounding_rectangle(tupla, (pil_im.size[0],pil_im.size[1]))
                pil_im_crop = pil_im.crop(tupla);
                pil_im_crop.save(os.path.join(path_incognita,filename+str(k)+".png"));
                k=k+1;
    elif (N==1):
        for annot in annotation:
            tupla=oppd.get_body_bounding_rectangle(annot.data, factor=1.4);
            if not((tupla[0]==0)and(tupla[1]==0)and(tupla[2]==0)and(tupla[3]==0)):
                tupla=oppd.get_valid_bounding_rectangle(tupla, (pil_im.size[0],pil_im.size[1]))
                pil_im_crop = pil_im.crop(tupla);
                pil_im_crop.save(os.path.join(path_paciente,filename+str(j)+".png"));
                j=j+1;
    
