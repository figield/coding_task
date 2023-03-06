import csv
import sys
# import re
# import shlex

def splitter(text):
    # return re.split(r',(?=")', text)
    # return [x.strip(',') for x in shlex.split(text)]
    return list(csv.reader([text], delimiter=',', quotechar='"'))[0]



def run():
    for line in ['1,2,3,"4,5",6,7', '1,2', '1,"a,b"']: #sys.stdin:
        line_list = splitter(line)
        line_list[0], line_list[1] = line_list[1], line_list[0]
        line_list = ['"{}"'.format(x) if ',' in x else x for x in line_list]
        sys.stdout.write(",".join(line_list) + "\n")


if __name__ == "__main__":
    run()