#include "advent.h"

#define TOKMAX	512

int	day2b_process(char *);

int
day2b(int argc, char **argv)
{
	FILE	*datafile;
	char	*linebuf = NULL;
	size_t	linelen;
	int	chksum = 0;

	if (argc != 1)
		errx(EXIT_FAILURE,"bad usage");

	if ((datafile = fopen(argv[0],"r")) == NULL)
		err(EXIT_FAILURE,"failed opening file");

	while (getline(&linebuf, &linelen, datafile) != -1) {
		chksum += day2b_process(linebuf);
	}

	if (feof(datafile) == 0)
		err(EXIT_FAILURE,"read failed");

	free(linebuf);

	if (fclose(datafile))
		err(EXIT_FAILURE,"failed to close file");

	printf("%d\n",chksum);

	return (EXIT_SUCCESS);
}

int
day2b_process(char *line)
{
	int	i, t, list[TOKMAX];
	char	*str;
	struct twodigits sorted;

	i = t = 0;

	chomp(line);

	for (i = 0, str = strtok(line," \t");
	    (i < TOKMAX) && (str);
	    str = strtok(NULL," \t"), i++, t++)
	{
		list[i] = strtol(str,NULL,0);
	}
	
	for (i = 0; i < t; i++) {
		for (int j = 0; j < t; j++) {
			if ((i == j) || (list[i] == list[j]))
				continue;
			sorted.left = list[i];
			sorted.right = list[j];
			sort_two_digits(&sorted);
			if ((sorted.left % sorted.right) == 0) {
				return (sorted.left / sorted.right);
			}
		}
	}

	return 0;
}
