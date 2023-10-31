# reader.py

import csv
import tracemalloc
from sys import intern
from collections import abc, defaultdict
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
    
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

class Data(abc.Sequence):
    def __init__(self, columns):
        self.names = list(columns)
        self.data = list(columns.values())
        
    def __len__(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return dict(zip(self.names,
                        (col[index] for col in self.data)))

def read_csv_as_dicts(filename, conversion):
    parser = DictCSVParser(conversion)
    port = parser.parse(filename)
    
    return port

def read_csv_as_columns(filename, conversion):
    columns = defaultdict(list)
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            for name, func, val in zip(headers, conversion, row):
                columns[name].append(func(val))
    
    return Data(columns)
      
def read_csv_as_instances(filename, cls):
    parser = InstanceCSVParser(cls)
    port = parser.parse(filename)
    
    return port