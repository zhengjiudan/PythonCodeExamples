import sys
import string

if len(sys.argv) != 2:
    print "Please input SES route files location config!";
    exit;

def GetSymbolNumber(ses_file_name):
    try:
        ses_file = open(ses_file_name);
        symbol_set = set();

        for line in ses_file:
            start = line.find('\x1e6\x1f')
            if start != -1:
                end = line.find('\x1e7\x1f', start);
                if end != -1:
                    symbol = line[start+3:end];
                    symbol_set.add(symbol);
                    
        ses_file.close();
        return len(symbol_set);
    except IOError, e:
        print e;
        return 0;

symbol_count = 0;
try:
    cnfg_file = open(sys.argv[1]);
except IOError, e:
    print e;
    exit(-1);

for ses_file_name in cnfg_file:
    ses_file_name = ses_file_name.strip('\n');
    ses_symbol_count = GetSymbolNumber(ses_file_name);
    print ses_file_name + ' has ' + str(ses_symbol_count) + ' symbols';
    symbol_count += ses_symbol_count;

print 'Total symbol count is ' + str(symbol_count);

cnfg_file.close();
