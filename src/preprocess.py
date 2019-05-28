# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

data = dict()
for line in sys.stdin:
    parts = line.strip().split(':')
    if len(parts) != 4:
        continue
    if not (parts[0][21:] in data.keys()):
        data[parts[0][21:]] = []
    data[parts[0][21:]].append((parts[0][0:21], parts[1]))
for k in data.keys():
    max_rssi = -1000.0
    max_pos = -1
    for i in range(len(data[k])):
        now_rssi = float(data[k][i][1])
        if now_rssi > max_rssi:
            max_rssi = now_rssi
            max_pos = i
    res = k
    start_pos = max_pos - 8
    end_pos = max_pos + 8
    '''
    if start_pos < 0:
        end_pos = end_pos - start_pos
        start_pos = 0
    elif end_pos > len(data[k]) - 1:
        start_pos = start_pos - (end_pos - len(data[k]) + 1)
        end_pos = len(data[k]) - 1
    '''
    if start_pos >= 0 and end_pos <= len(data[k]) - 1:
        for i in range(start_pos, end_pos + 1):
            res = res + ',' + data[k][i][1]
        print '%s\n' % res
