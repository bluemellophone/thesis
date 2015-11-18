#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


data_list = [
    (12, ('2', 'RED', 'E')),
    (13, ('3', 'PURPLE', 'A')),
    (20, ('15', 'WHITE', 'B')),
    (20, ('1', 'BLUE', 'D')),
    (22, ('16', 'WHITE', 'A')),
    (25, ('4', 'WHITE', 'A')),
    (35, ('1', 'PURPLE', 'C')),
    (36, ('15', 'WHITE', 'C')),
    (36, ('17', 'WHITE', 'A')),
    (39, ('4', 'RED', 'B')),
    (39, ('9', 'WHITE', 'A')),
    (45, ('1', 'BLUE', 'A')),
    (49, ('5', 'RED', 'C')),
    (53, ('17', 'WHITE', 'C')),
    (59, ('13', 'WHITE', 'A')),
    (62, ('12', 'WHITE', 'A')),
    (62, ('2', 'RED', 'D')),
    (62, ('3', 'PURPLE', 'B')),
    (63, ('1', 'BLUE', 'B')),
    (85, ('2', 'WHITE', 'A')),
    (86, ('25', 'PURPLE', 'A')),
    (103, ('7', 'WHITE', 'B')),
    (104, ('10', 'WHITE', 'A')),
    (105, ('1', 'WHITE', 'A')),
    (111, ('1', 'BLUE', 'C')),
    (116, ('3', 'RED', 'A')),
    (123, ('3', 'RED', 'B')),
    (128, ('15', 'WHITE', 'A')),
    (131, ('4', 'RED', 'A')),
    (138, ('1', 'WHITE', 'B')),
    (139, ('15', 'WHITE', 'D')),
    (141, ('5', 'WHITE', 'A')),
    (157, ('14', 'WHITE', 'A')),
    (163, ('7', 'WHITE', 'A')),
    (172, ('6', 'RED', 'A')),
    (178, ('13', 'WHITE', 'B')),
    (182, ('1', 'WHITE', 'C')),
    (198, ('1', 'RED', 'A')),
    (214, ('5', 'RED', 'A')),
    (241, ('11', 'WHITE', 'A')),
    (249, ('1', 'PURPLE', 'A')),
    (281, ('6', 'WHITE', 'B')),
    (325, ('1', 'RED', 'B')),
    (327, ('1', 'PURPLE', 'B')),
    (366, ('2', 'RED', 'B')),
    (381, ('8', 'WHITE', 'A')),
    (387, ('6', 'RED', 'B')),
    (388, ('3', 'WHITE', 'A')),
    (394, ('2', 'RED', 'C')),
    (455, ('1', 'PURPLE', 'D')),
    (459, ('2', 'RED', 'A')),
    # (1627, 'INITIAL DATABASE')
]


def get_xticks():
    return [
        # '%s %s %s' % _[1] if isinstance(_[1], tuple) else _[1]
        '%s' % _[1][0] if isinstance(_[1], tuple) else 'INITIAL'
        for _ in data_list
    ]


def get_letters():
    return [
        '%s' % _[1][2] if isinstance(_[1], tuple) else ''
        for _ in data_list
    ]


def get_yvalues(color):
    return [
        _[0] if color in _[1][1] or color in _[1] else 0
        for _ in data_list
    ]


def autolabel(rects, labels):
    # attach some text labels
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        if height == 0:
            continue
        # ax.text(rect.get_x() + rect.get_width() / 2., height + 20, '%d' % int(height),
        #         ha='center', va='bottom')
        ax.text(rect.get_x() + rect.get_width() / 2., height + 20, label,
                ha='center', va='bottom')


N = len(data_list)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots(figsize=(50, 5))
rects1 = ax.bar(ind, get_yvalues('RED'), width, color='r')
rects2 = ax.bar(ind, get_yvalues('BLUE'), width, color='b')
rects3 = ax.bar(ind, get_yvalues('WHITE'), width, color='w')
rects4 = ax.bar(ind, get_yvalues('PURPLE'), width, color=(0.5019607843137255, 0.0, 0.5019607843137255))
rects5 = ax.bar(ind, get_yvalues('INITIAL'), width, color='g')

autolabel(rects1, get_letters())
autolabel(rects2, get_letters())
autolabel(rects3, get_letters())
autolabel(rects4, get_letters())
autolabel(rects5, get_letters())

# add some text for labels, title and axes ticks
ax.set_xticks(ind + width)
ax.set_xticklabels( get_xticks() )
ax.set_xlim([-1, len(data_list)])

plt.show()
