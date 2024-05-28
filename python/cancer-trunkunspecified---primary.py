# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"ZV10y00","system":"readv2"},{"code":"B23y.00","system":"readv2"},{"code":"B31y.00","system":"readv2"},{"code":"B10y.00","system":"readv2"},{"code":"B08y.00","system":"readv2"},{"code":"B06y.00","system":"readv2"},{"code":"ByuD300","system":"readv2"},{"code":"B54y.00","system":"readv2"},{"code":"B60y.00","system":"readv2"},{"code":"B325z00","system":"readv2"},{"code":"B17yz00","system":"readv2"},{"code":"B325.00","system":"readv2"},{"code":"B55yz00","system":"readv2"},{"code":"B13y.00","system":"readv2"},{"code":"ByuC000","system":"readv2"},{"code":"B17y.00","system":"readv2"},{"code":"B05y.00","system":"readv2"},{"code":"By...00","system":"readv2"},{"code":"B06yz00","system":"readv2"},{"code":"B45y.00","system":"readv2"},{"code":"B21y.00","system":"readv2"},{"code":"B62x.00","system":"readv2"},{"code":"B11y.00","system":"readv2"},{"code":"B32y.00","system":"readv2"},{"code":"B335.00","system":"readv2"},{"code":"B33y.00","system":"readv2"},{"code":"B12y.00","system":"readv2"},{"code":"Byu8000","system":"readv2"},{"code":"B11yz00","system":"readv2"},{"code":"B07y.00","system":"readv2"},{"code":"B67..00","system":"readv2"},{"code":"B52y.00","system":"readv2"},{"code":"Byu1100","system":"readv2"},{"code":"Byu7100","system":"readv2"},{"code":"ByuD800","system":"readv2"},{"code":"B335z00","system":"readv2"},{"code":"B55y100","system":"readv2"},{"code":"B18y.00","system":"readv2"},{"code":"B67z.00","system":"readv2"},{"code":"B55y.00","system":"readv2"},{"code":"B18yz00","system":"readv2"},{"code":"C00-C75","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-trunkunspecified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-trunkunspecified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-trunkunspecified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
