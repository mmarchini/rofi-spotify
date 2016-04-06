
from subprocess import Popen, PIPE


def rofi(items=[], prefix=''):
    items_str = '\n'.join([i.encode('utf-8') for i in items])
    p = Popen(['rofi', '-dmenu', '-p', prefix], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    selected, _ = p.communicate(items_str)

    return unicode(selected.strip(), 'utf-8')
