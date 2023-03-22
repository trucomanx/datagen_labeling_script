#!/usr/bin/python

## pip3 install natsort

import sys
sys.path.append('../../libraries/WorkingWithFiles/src');
import WorkingWithFiles as rnfunc

#######################################################################
## python csv_generator.py --format .png --csv-file labels.csv --base-dir /my/path
#######################################################################
csv_file='labels.csv';
base_dir='/mnt/c/Dados/Fernando/DATASET/fer2013-fpr2023/archive/test';
default_format='.png';

format_list=[];
for n in range(len(sys.argv)):
    if sys.argv[n]=='--csv-file':
        csv_file=sys.argv[n+1];
    if sys.argv[n]=='--base-dir':
        base_dir=sys.argv[n+1];
    if sys.argv[n]=='--format':
        format_list.append(sys.argv[n+1]);

if len(format_list)==0:
    format_list=[default_format];

print('')
print('   csv_file:',csv_file)
print('   base_dir:',base_dir)
print('format_list:',format_list)
print('')

rnfunc.generate_csv_file_from_dir_structure(base_dir,format_list,csv_file);
