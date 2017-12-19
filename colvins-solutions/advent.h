#ifndef ADVENT_H
#define ADVENT_H

#define _WITH_GETLINE

#include <ctype.h>
#include <err.h>
#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define CMP(x,y)	(strcmp(x,y) == 0)

struct twodigits {
	int	left;
	int	right;
};

int	day1a(int, char **);
int	day1b(int, char **);
int	day2a(int, char **);
int	day2b(int, char **);
int	day3a(int, char **);

int	chomp(char *);
void	sort_two_digits(struct twodigits *);

#endif
