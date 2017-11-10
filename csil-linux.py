#!/usr/bin/env python3

import subprocess
import random
import re

ttlre = re.compile(b" ttl=(\\d+) ")

rooms = [ # roomid, rows, columns, domain
    ('asb9700u', 5, 8, 'csil.sfu.ca'),
    ('asb9838nu', 5, 16, 'csil.sfu.ca'),
    ('asb9804u', 4, 8, 'csil.sfu.ca'),
    ('asb9820u', 4, 5, 'csil.sfu.ca'),
    ('asb9840u', 5, 8, 'csil.sfu.ca'),
    ('cs-sc4050', 4, 8, 'cs.surrey.sfu.ca'),
    #('asb10928', 5, 7, 'csil.sfu.ca')
]


def check_host(host):
    """
    Return OS signature of this host
    """
    # http://www.kellyodonnell.com/content/determining-os-type-ping
    process = subprocess.Popen(['ping', '-c', '1', '-w', '1', host],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    resp = process.returncode
    m = ttlre.search(out)
    if m:
        ttl = int(m.group(1))
        if ttl < 32:
            return 'mac'
        elif ttl < 64:
            return 'linux'
        elif ttl < 128:
            return 'windows'
        else:
            return '???'
    return None

	        
def get_all_hosts():
    """
    All hostnames we want to check
    """
    for rm, maxr, maxc, domain in rooms:
        for r in range(maxr):
            l = "abcdefg"[r]
            for c in range(maxc):
                yield "%s-%s%02i.%s" % (rm, l, c+1, domain)


all_hosts = list(get_all_hosts())
#print(','.join(h+'.csil.sfu.ca' for h in all_hosts))

living_hosts = [h for h in all_hosts if check_host(h)=='linux']
print('%i of %i currently in Linux:' % (len(living_hosts), len(all_hosts)))

#random.shuffle(living_hosts)
print('\n'.join(living_hosts))


