#!/usr/bin python3

import csv

COL_TAXONID = 0
COL_NAME = 2
COL_LANGUAGE = 4
PATH_TSV = "VernacularName.tsv"
PATH_LINES = "lines.txt"
TARGET_LANGUAGE = "eng"


def main():
    # open in and out files
    with open(PATH_TSV, newline="") as tsvfile, open(PATH_LINES, "w") as lines_file:
        # create tsv reader
        tsvreader = csv.reader(tsvfile, delimiter="\t")

        taxonid_group = ""
        taxonid_uniq = set()

        # skip header row
        next(tsvreader)
        for row in tsvreader:
            # filter on target language
            if row[COL_LANGUAGE] != TARGET_LANGUAGE:
                continue

            name = row[COL_NAME]

            taxonid = row[COL_TAXONID]
            if taxonid != taxonid_group:
                taxonid_group = taxonid
                taxonid_uniq.clear()
            elif name in taxonid_uniq:
                continue
            
            taxonid_uniq.add(name)
            lines_file.write(name + "\n")


if __name__ == "__main__":
    main()
