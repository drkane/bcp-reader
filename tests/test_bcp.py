import os
import csv
import io
import bcp

testfile = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'testfile.bcp'
)
testcsv = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'testfile.csv'
)


def test_reader():
    with open(testfile) as a:
        reader = bcp.reader(a)
        for r in reader:
            assert type(r) == list
            assert len(r) == 12
            if r[0] == '13':
                assert r[3] == 'Saundercock, Mr. William Henry'


def test_dict_reader():
    with open(testfile) as a:
        reader = bcp.DictReader(a)
        for r in reader:
            assert type(r) == dict
            assert len(r) == 12
            if r['PassengerId'] == '13':
                assert r['Name'] == 'Saundercock, Mr. William Henry'


def test_dict_reader_fieldnames():
    dummy_fields = ["field {}".format(x) for x in range(12)]
    with open(testfile) as a:
        reader = bcp.DictReader(a, fieldnames=dummy_fields)
        for r in reader:
            assert type(r) == dict
            assert len(r) == 12
            if r['field 0'] == '13':
                assert r['field 3'] == 'Saundercock, Mr. William Henry'


def test_reader_linenum():
    with open(testfile) as a:
        reader = bcp.reader(a)
        for i, r in enumerate(reader):
            assert i+1 == reader.line_num


def test_dictreader_linenum():
    with open(testfile) as a:
        reader = bcp.DictReader(a)
        for i, r in enumerate(reader):
            assert i+2 == reader.line_num


def test_reader_small_blocksize():
    with open(testfile) as a:
        reader = bcp.reader(a, blocksize=12)
        for r in reader:
            assert type(r) == list
            assert len(r) == 12
            if r[0] == '13':
                assert r[3] == 'Saundercock, Mr. William Henry'


def test_dict_reader_small_blocksize():
    with open(testfile) as a:
        reader = bcp.DictReader(a, blocksize=12)
        for r in reader:
            assert type(r) == dict
            assert len(r) == 12
            if r['PassengerId'] == '13':
                assert r['Name'] == 'Saundercock, Mr. William Henry'


def test_csv_output():
    with open(testfile, 'rb') as a:
        dummy = io.StringIO(newline='')
        writer = csv.writer(dummy)
        r = bcp.reader(io.TextIOWrapper(a, encoding='utf8'))
        writer.writerows(r)
        dummy.seek(0)
        with open(testcsv) as b:
            b_lines = b.readlines()
            for i, d in enumerate(dummy.readlines()):
                assert d.strip() == b_lines[i].strip()
