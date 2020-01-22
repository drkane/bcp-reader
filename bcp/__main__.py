import sys
import argparse
import csv
import bcp


def main():
    parser = argparse.ArgumentParser(description='Convert a BCP file into a CSV')
    parser.add_argument('infile', help="file to convert")
    parser.add_argument('--encoding', '-e', default='latin1', help='Encoding of the file to convert')
    args = parser.parse_args()
    writer = csv.writer(sys.stdout)
    with open(args.infile, 'r', encoding=args.encoding) as a:
        writer.writerows(bcp.reader(a))

if __name__ == '__main__':
    main()
