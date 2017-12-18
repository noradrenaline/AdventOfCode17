#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622, W0621, W0603

r"""
Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
In this example, the following programs are in the group that contains program ID 0:

Program 0 by definition.
Program 2, directly connected to program 0.
Program 3 via program 2.
Program 4 via program 2.
Program 5 via programs 6, then 4, then 2.
Program 6 via programs 4, then 2.
Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?
"""

import fileinput
import py2neo

NODES = {}
RELATIONSHIPS = {}
GRAPH = py2neo.database.Graph(user='singram',
                              password='test')

GRAPH.run('match (n:Program)-[r]-() DELETE n, r')

GRAPH.begin()
tx = GRAPH.begin()


def import_node(line):
    source, dests = line.strip().split(' <-> ')
    if source not in NODES:
        NODES[source] = py2neo.Node("Program", number=source)
        tx.create(NODES[source])
    for dest in dests.split(', '):
        if dest not in NODES:
            NODES[dest] = py2neo.Node("Program", number=dest)
            tx.create(NODES[dest])
        if (source, dest) not in RELATIONSHIPS:
            RELATIONSHIPS[(source, dest)] = py2neo.Relationship(NODES[source],
                                                                "COMMUNICATES",
                                                                NODES[dest])
            tx.create(RELATIONSHIPS[(source, dest)])


for line in fileinput.input():
    import_node(line)

tx.commit()

data = GRAPH.run(
    'match (n:Program {number: "0"}) call apoc.path.subgraphNodes(n, {}) YIELD node RETURN count(distinct node)')
print next(data).values()[0]

data = GRAPH.run('CALL algo.unionFind.stream("Program", "COMMUNICATES", {}) YIELD nodeId,setId RETURN count(distinct setId)')
print next(data).values()[0]
