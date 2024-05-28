# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"B004000","system":"readv2"},{"code":"B00z100","system":"readv2"},{"code":"B621000","system":"readv2"},{"code":"Byu9000","system":"readv2"},{"code":"B5...00","system":"readv2"},{"code":"B116.00","system":"readv2"},{"code":"B152.00","system":"readv2"},{"code":"B1zy.00","system":"readv2"},{"code":"B115.00","system":"readv2"},{"code":"Byu2500","system":"readv2"},{"code":"B627X00","system":"readv2"},{"code":"B62z600","system":"readv2"},{"code":"Byu4100","system":"readv2"},{"code":"B24X.00","system":"readv2"},{"code":"B623000","system":"readv2"},{"code":"B624000","system":"readv2"},{"code":"B62z400","system":"readv2"},{"code":"B143.00","system":"readv2"},{"code":"Byu5800","system":"readv2"},{"code":"B0z0.00","system":"readv2"},{"code":"B68..00","system":"readv2"},{"code":"B620000","system":"readv2"},{"code":"Byu7300","system":"readv2"},{"code":"B62z800","system":"readv2"},{"code":"B316.00","system":"readv2"},{"code":"B614000","system":"readv2"},{"code":"Byu5300","system":"readv2"},{"code":"Byu3300","system":"readv2"},{"code":"B5...11","system":"readv2"},{"code":"B2z0.00","system":"readv2"},{"code":"B62z000","system":"readv2"},{"code":"B625000","system":"readv2"},{"code":"ByuA000","system":"readv2"},{"code":"B057.00","system":"readv2"},{"code":"ByuDE00","system":"readv2"},{"code":"Byu4300","system":"readv2"},{"code":"B05..00","system":"readv2"},{"code":"B613000","system":"readv2"},{"code":"B1z0.00","system":"readv2"},{"code":"B007.00","system":"readv2"},{"code":"Byu4000","system":"readv2"},{"code":"B615000","system":"readv2"},{"code":"B62y000","system":"readv2"},{"code":"Byu5400","system":"readv2"},{"code":"B62z100","system":"readv2"},{"code":"ByuD900","system":"readv2"},{"code":"B59zX00","system":"readv2"},{"code":"B323.00","system":"readv2"},{"code":"B627W00","system":"readv2"},{"code":"ByuDC00","system":"readv2"},{"code":"Byu8200","system":"readv2"},{"code":"ByuDF00","system":"readv2"},{"code":"B62z500","system":"readv2"},{"code":"B62z300","system":"readv2"},{"code":"B626000","system":"readv2"},{"code":"B333z00","system":"readv2"},{"code":"B014.00","system":"readv2"},{"code":"B68y.00","system":"readv2"},{"code":"ByuA200","system":"readv2"},{"code":"B004200","system":"readv2"},{"code":"B52..00","system":"readv2"},{"code":"B333.00","system":"readv2"},{"code":"B4A..00","system":"readv2"},{"code":"B601000","system":"readv2"},{"code":"Byu2000","system":"readv2"},{"code":"Byu5100","system":"readv2"},{"code":"ByuDD00","system":"readv2"},{"code":"B454.00","system":"readv2"},{"code":"Byu1200","system":"readv2"},{"code":"B616000","system":"readv2"},{"code":"B52X.00","system":"readv2"},{"code":"B61z000","system":"readv2"},{"code":"B62xX00","system":"readv2"},{"code":"ByuA100","system":"readv2"},{"code":"B600000","system":"readv2"},{"code":"Byu5700","system":"readv2"},{"code":"B00z000","system":"readv2"},{"code":"B004.00","system":"readv2"},{"code":"B483.00","system":"readv2"},{"code":"Byu7000","system":"readv2"},{"code":"B67yz00","system":"readv2"},{"code":"B055.00","system":"readv2"},{"code":"B54X.00","system":"readv2"},{"code":"B45..00","system":"readv2"},{"code":"B67y.00","system":"readv2"},{"code":"B40..00","system":"readv2"},{"code":"ZV10z00","system":"readv2"},{"code":"Byu5900","system":"readv2"},{"code":"C85","system":"readv2"},{"code":"C95","system":"readv2"},{"code":"C96","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-unspecif---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-unspecif---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-unspecif---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
