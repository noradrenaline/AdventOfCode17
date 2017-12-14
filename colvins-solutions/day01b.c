#include "advent.h"

int
day1b(int argc, char **argv)
{
	int	sum, offset;
	char	*input;
	size_t	len;

	if (argc != 1)
		errx(EXIT_FAILURE,"bad usage");

	sum = 0;

	input = argv[0];
	len = strlen(input);

	if ((len % 2) != 0)
		errx(EXIT_FAILURE,"bad data: not even");

	offset = (len/2);

	for (int i = 0; i < len; i++) {
		if (!isdigit(input[i]))
			errx(EXIT_FAILURE,"bad data: not a digit");
#if 1
		int this = input[i] - '0';
		int j = ((i + offset) < len) ? (i + offset) : ((i + offset) - len);
		int next = input[j] - '0';
		if (this == next)
			sum += this;
#else
		/* this also works */
		if ((input[i] - '0') == (input[((i + offset) < len) ? (i + offset) : ((i + offset) - len)] - '0'))
			sum += input[i] - '0';
#endif
	}

	printf("%d\n",sum);

	return (EXIT_SUCCESS);
}
