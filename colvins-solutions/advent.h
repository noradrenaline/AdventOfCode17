#ifndef ADVENT_H
#define ADVENT_H

#include <ctype.h>
#include <err.h>
#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define CMP(x,y)	(strcmp(x,y) == 0)

int	day1a(int, char **);
int	day1b(int, char **);

#endif
