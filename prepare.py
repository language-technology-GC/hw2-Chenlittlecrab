#!/usr/bin/env python
"""This script preprocesses the tsv files."""

import csv
import argparse

def main(args: argparse.Namespace):
    with open(args.input, "r") as source, open(args.output_g, "w") as sink_g, open(
        args.output_p, "w"
        ) as sink_p:
        for col_g, col_p in csv.reader(source, delimiter = "\t"):
            print(" ".join(col_g), file = sink_g)
            print(col_p, file = sink_p)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Provide the name for the input file")
    parser.add_argument("output_g", help="Provide the name for the output grapheme file")
    parser.add_argument("output_p", help="Provide the name for the output phoneme file")
    main(parser.parse_args())