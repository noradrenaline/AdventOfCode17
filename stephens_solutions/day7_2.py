#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622, W0621

r"""
The programs explain the situation: they can't get down. Rather, they could get
down, if they weren't expending all of their energy trying to keep the tower
balanced. Apparently, one program has the wrong weight, and until it's fixed,
they're stuck here.

For any program holding a disc, each program standing on that disc forms a
sub-tower. Each of those sub-towers are supposed to be the same weight, or the
disc itself isn't balanced. The weight of a tower is the sum of the weights of
the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo,
ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc
and all programs above it must each match. This means that the following sums
must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
other two. Even though the nodes above ugml are balanced, ugml itself is too
heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the
towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need
to be to balance the entire tower?
"""

import fileinput
from collections import defaultdict


class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.full_weight = None
        self.children = set()

    def get_weight(self, nodes):
        if not self.full_weight:
            child_weight = sum([nodes[i].get_weight(nodes)
                                for i in self.children])
            self.full_weight = self.weight + child_weight
        return self.full_weight

    def is_balanced(self, nodes):
        return len(set(nodes[i].get_weight(nodes)
                       for i in self.children)) == 1 if self.children else True

    def children_balanced(self, nodes):
        return all(nodes[i].is_balanced(nodes)
                   for i in self.children) if self.children else True

    def get_deficit(self, nodes):
        weight_dict = defaultdict(list)
        for child in self.children:
            weight_dict[nodes[child].get_weight(nodes)] += [nodes[child].name]
        balanced_node = nodes[[weight_dict[i]
                               for i in weight_dict if len(weight_dict[i]) > 1][0][0]]
        unbalanced_node = nodes[[weight_dict[i]
                                 for i in weight_dict if len(weight_dict[i]) == 1][0][0]]
        return unbalanced_node.weight + balanced_node.get_weight(nodes) - unbalanced_node.get_weight(nodes)

    def __repr__(self):
        return '{} : {}'.format(self.name, self.weight)


def proc_line(line):
    if line.find('->') > -1:
        pfield, children = line.strip().split(' -> ')
        children = children.strip().split(', ')
    else:
        pfield = line.strip()
        children = []
    program_name, paren_weight = pfield.split(' ')
    return (program_name, int(paren_weight[1:-1]), children)


def make_nodes(input):
    nodes = {}
    for line in input:
        program_name, weight, children = proc_line(line)
        nodes[program_name] = Node(program_name, weight)
        nodes[program_name].children = set(children)
    return nodes


nodes = make_nodes(fileinput.input())
print [nodes[node].get_deficit(nodes)
       for node in nodes
       if not nodes[node].is_balanced(nodes) and nodes[node].children_balanced(nodes)][0]
