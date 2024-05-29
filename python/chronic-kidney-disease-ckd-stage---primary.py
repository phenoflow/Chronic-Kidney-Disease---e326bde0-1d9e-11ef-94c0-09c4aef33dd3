# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Ian Buchan, Mamas A Mamas, Naveed Sattar, Darren M Ashcroft, Martin M Rutter, 2024.

import sys, csv, re

codes = [{"code":"K054.00","system":"readv2"},{"code":"K051.00","system":"readv2"},{"code":"1Z16.00","system":"readv2"},{"code":"K053.00","system":"readv2"},{"code":"1Z15.00","system":"readv2"},{"code":"1Z14.00","system":"readv2"},{"code":"K052.00","system":"readv2"},{"code":"1Z10.00","system":"readv2"},{"code":"1Z12.00","system":"readv2"},{"code":"1Z11.00","system":"readv2"},{"code":"1Z13.00","system":"readv2"},{"code":"K055.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-kidney-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-kidney-disease-ckd-stage---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-kidney-disease-ckd-stage---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-kidney-disease-ckd-stage---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
