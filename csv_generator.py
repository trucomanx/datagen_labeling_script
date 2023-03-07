#!/usr/bin/python

import sys
sys.path.append('/mnt/c/Dados/Fernando/CODE/PESQUISA/libraries/WorkingWithFiles/src');

import WorkingWithFiles as rnfunc

csv_path='labels.csv';
base_dir='/mnt/c/Dados/Fernando/DATASET/fer2013-fpr2023/archive/test';

format_list=['.png'];

rnfunc.generate_csv_file_from_dir_structure(base_dir,format_list,csv_path);
