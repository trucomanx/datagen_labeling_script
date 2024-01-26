#!/usr/bin/python

import os
import sys

## Para cada image con varias personas: Divide en varias imagens con una persona por imagen.
## El resultado es colocado en 'output'

"""
git clone https://github.com/trucomanx/WorkingWithFiles.git
cd WorkingWithFiles/src
python setup.py sdist
pip3 install dist/WorkingWithFiles-*.tar.gz
"""
import WorkingWithFiles as rnfunc

sys.path.append('/home/fernando/Proyectos/PÓS-GRADUAÇÂO/TESIS-DOUTORADO-2/PESQUISA/software/OpenpifpafTools/library');
import OpenpifpafPeople as oppp

basedir='/mnt/boveda/DATASETs/PATIENT-IMAGES/dataset_800/anger';
formats_search=['.jpeg','.JPEG','.jpg','.JPG']
path_salida='output'
prename="filename";
init_id=1;
output_ext=".png";


################################################################################
total=rnfunc.get_all_files_in_dir_list([basedir],formats_search=formats_search);

try: 
    os.mkdir(path_salida) 
except: 
    pass


k=init_id;
for filepath in total:
    print(filepath)
    
    pil_list = oppp.get_pil_images_with_people(filepath);
    
    for pil_im_crop in pil_list:
        pil_im_crop.save(os.path.join(path_salida,prename+str(k)+output_ext));
        k=k+1;
            

