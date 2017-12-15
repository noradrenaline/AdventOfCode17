#include "advent.h"

int	day2a_process(char *);

int
day2a(int argc, char **argv)
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
		chksum += day2a_process(linebuf);
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
day2a_process(char *line)
{
	int	min, max;
	char	*str;

	min = max = 0;

	chomp(line);

	for (str = strtok(line," \t"), min = strtol(str,NULL,0); str; str = strtok(NULL," \t")) {
		int this = strtol(str,NULL,0);
		if (this < min)
			min = this;
		if (this > max)
			max = this;
	}

	return (max - min);
}
