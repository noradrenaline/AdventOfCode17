#include "advent.h"

int
main(int argc, char **argv)
{
	int	r;
	char	*problem;

	if (argc < 2)
		errx(EXIT_FAILURE,"usage: %s <problem> ...",argv[0]);

	problem = strdup(argv[1]);

	argc -= 2;
	argv += 2;

	if (CMP(problem,"1a"))
		r = day1a(argc, argv);
	else if (CMP(problem,"1b"))
		r = day1b(argc, argv);
	else
		errx(EXIT_FAILURE,"bad problem");

	free(problem);

	return (r);
}
