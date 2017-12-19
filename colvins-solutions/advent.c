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
	else if (CMP(problem,"2a"))
		r = day2a(argc, argv);
	else if (CMP(problem,"2b"))
		r = day2b(argc, argv);
	else if (CMP(problem,"3a"))
		r = day3a(argc, argv);
	else
		errx(EXIT_FAILURE,"bad problem");

	free(problem);

	return (r);
}

int
chomp(char *str)
{
	int	c = 0;
	size_t	l = 0;

	if (str == NULL)
		return (0);

	l = strlen(str);
	if (l == 0)
		return (0);

	while (str[l-1] == '\n') {
		str[l-1] = '\0';
		l--;
		c++;
	}

	return (c);
}

void
sort_two_digits(struct twodigits *a)
{
	int	tmp = 0;

	if (a->left > a->right)
		return;
	else {
		tmp = a->right;
		a->right = a->left;
		a->left = tmp;
	}
	return;
}
