#include "advent.h"

int
day1a(int argc, char **argv)
{
	int	prev, sum;
	size_t	len;
	char	*input;

	prev = sum = 0;

	if (argc != 1)
		errx(EXIT_FAILURE,"bad usage");

	input = argv[0];

	len = strlen(input);
	for (int i = 0; i < len; i++) {
		if (!isdigit(input[i]))
			errx(EXIT_FAILURE,"bad data");

		int this = input[i] - '0';

		if (i == 0) {
			if (input[0] == input[len - 1])
				sum += this;
		} else {
			if (this == prev)
				sum += this;
		}
		prev = this;
	}

	printf("%d\n",sum);

	free(input);

	return (EXIT_SUCCESS);
}
