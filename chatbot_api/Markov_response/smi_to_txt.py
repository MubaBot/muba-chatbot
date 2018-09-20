# -*- coding: utf-8 -*-
import sys,os



output_file_name = 'smi.txt'#sys.argv[1]

f_out = open(output_file_name, 'w')
smi_dir='./smi'
filenames = os.listdir(smi_dir)
for input_file_name in filenames:
    if input_file_name=='.' and input_file_name=='..':
        continue
    print(input_file_name)
    with open(smi_dir+'/'+input_file_name, "r") as f_in:
        lines = [line for line in f_in]
        # print(lines)
        tt=0
        if input_file_name.endswith('.smi'):
            for idx,line in enumerate(lines):
                if tt==0:
                    if line.startswith('<SYNC'):
                        tt=1

                        continue
                if tt==1:
                    tt=0
                    if line.startswith('<SYNC'):
                        tt=1
                        continue
                    f_out.write((line.replace('<br>','\n') + '\n').replace('\n\n','\n'))




    f_in.close()
f_out.close()