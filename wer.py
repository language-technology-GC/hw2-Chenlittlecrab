#!/usr/bin/env python

"""Computes word error rates of the prediction txt files"""

import csv
import argparse
import logging

def txt_reader(input_path):
    ls_origin = []
    ls_predict = []
    with open(input_path, "r") as source:
        for row in csv.reader(source, delimiter = "\t"):
            if row[0].startswith("T"):
                ls_origin.append(row[-1])
            if row[0].startswith("H"):
                ls_predict.append(row[-1])
    return ls_origin, ls_predict

def main(args: argparse.Namespace):
    total = 0
    counter = 0
    origin_word, predict_word = txt_reader(args.input)
    for word1, word2 in zip(origin_word, predict_word):
        total +=1
        if word1 != word2:
            counter +=1
    WER = counter / total
    logging.info("WES: \t%.2f", WER)

if __name__ =="__main__":
    logging.basicConfig(level = "INFO", format = "%(levelname)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Provide the directory for the input file")
    main(parser.parse_args())
    


