import traceback
import sys
from logs.models import Error


def error_log(file, category=None, user=None, ip=None):
    type_, value, _traceback = sys.exc_info()
    output = 'Type: {} \n Value: {} \n'.format(type_, value)
    trace = traceback.extract_tb(sys.exc_info()[2])
    # Add the event to the log
    output += 'Traceback is: \n'
    for (file, linenumber, affected, line) in trace:
        output += '- Error at function {}\n'. format(affected)
        output += '- At: {} {}\n'. format(file, linenumber)
        output += '- Source: {}\n\n'.format(line)
    return Error.objects.create(url=file, error=output, category=category, ip=ip, user=user)