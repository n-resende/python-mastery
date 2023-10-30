# reader.py

import csv
import tracemalloc
from sys import intern
from collections import abc, defaultdict

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
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        data = []
        for row in rows:
            data.append( {name:func(val) for name, func, val in zip(headers, conversion, row)} )
    
    return data

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
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
            
if __name__ == '__main__':
    portfolio = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
    for s in portfolio:
        print(s)
    
    tracemalloc.start()
    rows = read_csv_as_columns('Data/ctabus.csv', [intern, intern, str, int])
    print(len(rows))
    print(rows[0])
    print(tracemalloc.get_traced_memory())