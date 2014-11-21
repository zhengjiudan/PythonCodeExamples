import sys
import string

if len(sys.argv) != 3:
    print "Please input source file name and RIC mapping file name!";
    exit;

float_file = open(sys.argv[1]);
ric_dic = {};

ric_file = open(sys.argv[2]);
for line in ric_file:
    line.strip('\n');
    str_arr = line.split(',');
    if len(str_arr) > 1 and len(str_arr[0]) > 0:
        ric_dic[str_arr[0]] = str_arr[1];
        print str_arr[1];
#        print line;

ric_file.close();

result_file = open("result.txt", 'w');

for line in float_file:
    line.replace('<', '');
    line.replace('>', '');
    str_arr_line = line.split('|');
    if len(str_arr_line) < 22:
        continue;
    if str_arr_line[1] != 'PX4':
        continue;
    if ric_dic.has_key(str_arr_line[3]):
        result_file.write(ric_dic[str_arr_line[3]] + ": " + str_arr_line[8] + ", " + str_arr_line[19]);
        result_file.write('\n');

float_file.close();
result_file.close();
