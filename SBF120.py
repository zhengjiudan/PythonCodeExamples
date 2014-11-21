import sys
import string

if len(sys.argv) != 3:
    print "Please input result file name and float file name!";
    exit;

file_object = open(sys.argv[1]);

expect_ask_volume = False;
expect_hst_close = False;
expect_trd_prc1 = False;
has_ask_volume = False;
has_hst_close = False;
has_trd_prc1 = False;
ask_volume = 0;
hst_close = 0.0;
trd_prc1 = 0.0;
RIC=''
summ = 0.0;

float_file = open(sys.argv[2]);

for line in float_file:
    line.replace('<', '');
    line.replace('>', '');
    str_arr_line = line.split(' ');
    if str_arr_line.length
    float_dic[str_arr_line[2]) = string.atof(str_arr_line[3]);
    float_dic[str_arr_line[4]) = string.atof(str_arr_line[5]);
    float_dic[str_arr_line[6]) = string.atof(str_arr_line[7]);
    float_dic[str_arr_line[8]) = string.atof(str_arr_line[9]);
    

for line in file_object:
    if line.find('ASK_VOLUME') >= 0:
        expect_ask_volume = True;
        continue;
    elif line.find('HST_CLOSE') >= 0:
        expect_has_hst_close = True;
        continue;
    elif line.find('TRDPRC_1') >= 0:
        expect_trd_prc1 = True;
        continue;
    elif line.find('RIC') == 0:
        str_arr = line.split('=');
        RIC = str_arr.replace(' ', '')

    if line.find('R_VOLUME') >= 0:
        if expect_ask_volume:
            has_ask_volume = True;
            expect_ask_volume = False;
            str_arr = line.split('=');
            ask_volume = string.atoi(str_arr[1]);
    elif line.find('R_PRICE') >= 0:
        if expect_hst_close:
            has_hst_close = True;
            expect_has_hst_close = False;
            str_arr = line.split('=');
            hst_close = string.atof(str_arr[1]);
        elif expect_trd_prc1:
            has_trd_prc1 = True;
            expect_trd_prc1 = False;
            str_arr = line.split('=');
            trd_prc1 = string.atof(str_arr[1]);

    if has_ask_volume and has_trd_prc1:
        if trd_prc1 != 0.0:
            print 'TRDPRC1: %d * %f' %(ask_volume,trd_prc1);
            summ = summ + ask_volume * trd_prc1;
        elif has_hst_close:
            print 'HST_CLOSE: %d * %f' %(ask_volume,hst_close);
            summ = summ + ask_volume * hst_close;

        has_ask_volume = False;
        has_hst_close = False;
        has_trd_prc1 = False;
        ask_volume = 0;
        hst_close = 0.0;
        trd_prc1 = 0.0;
        RIC = ''
            
print '%f'% summ

file_object.close();
