#!/usr/bin/python

import sys
sys.path.append('/home/fernando/Downloads/TESIS-DOUTORADO-2/PESQUISA/libraries/WorkingWithFiles/src');

import WorkingWithFiles as rnfunc

csv_path='labels.csv';
base_dir='/mnt/boveda/DATASETs/FACE-EMOTION/AffectNet-Sample/input/affectnetsample/train_class';

format_list=['.jpg'];

rnfunc.generate_csv_file_from_dir_structure(base_dir,format_list,csv_path);
