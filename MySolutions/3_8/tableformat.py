from abc import ABC, abstractmethod

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
    
class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(*headers, sep=',')
    
    def row(self, rowdata):
        print(*rowdata, sep=',')
    
class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr> ' + ''.join('<th>%s</th> ' % h for h in headers) + '</tr>')
    
    def row(self, rowdata):
        print('<tr> ' + ''.join('<th>%s</th> ' % d for d in rowdata) + '</tr>')
        
class NewFormatter(TableFormatter):
    def headers(self, headers):
        pass
    def row(self, rowdata):
        pass   

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError(f"Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
        
def create_formatter(type, column_formats=None, upper_headers=False):
    if type == 'text':
        formatter = TextTableFormatter
    elif type == 'csv':
        formatter = CSVTableFormatter
    elif type == 'html':
        formatter = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {type}')
    
    if column_formats:
        class formatter(ColumnFormatMixin, formatter):
            formats = column_formats
    
    if upper_headers:
        class formatter(UpperHeadersMixin, formatter):
            pass
    
    return formatter()
        
