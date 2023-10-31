
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

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

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
        
def create_formatter(type):
    if type == 'text':
        formatter = TextTableFormatter
    elif type == 'csv':
        formatter = CSVTableFormatter
    elif type == 'html':
        formatter = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {type}')
    return formatter()
        
