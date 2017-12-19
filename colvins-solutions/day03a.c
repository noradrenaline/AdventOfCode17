#include "advent.h"

struct coordinate {
	int	x;
	int	y;
};

struct coordinate *create_coordinate(int, int);

void turn_left(void);

enum cartesian {
	EAST,
	NORTH,
	WEST,
	SOUTH
};

enum cartesian direction;

int
day3a(int argc, char **argv)
{
	int	input, turn;
	struct coordinate **grid, *last;

	if (argc != 1)
		errx(EXIT_FAILURE,"bad usage");

	input = strtol(argv[0],NULL,0);

	grid = calloc(input + 1, sizeof(struct coordinate *));

	grid[0] = NULL;
	grid[1] = create_coordinate(0,0);
	last = create_coordinate(0,0);

	direction = EAST;
	turn = 1;

	for (int i = 2, c = 1, d = 1; i <= input; i++, c++) {
		int x = last->x;
		int y = last->y;
		switch (direction) {
			case EAST:	x++; break;
			case NORTH:	y++; break;
			case WEST:	x--; break;
			case SOUTH:	y--; break;
		}
		grid[i] = create_coordinate(x,y);
		last->x = x;
		last->y = y;
		if (c == turn) {
			turn_left();
			if (d % 2 == 0) {
				turn++;
				d = 0;
			}
			d++;
			c = 0;
		}
	}

	printf("%d\n",(abs(grid[input]->x) + abs(grid[input]->y)));

	for (int i = input; i >= 0; i--)
		free(grid[i]);

	free(grid);
	free(last);

	return (EXIT_SUCCESS);
}

struct coordinate *
create_coordinate(int x, int y)
{
	struct coordinate *c;

	if ((c = malloc(sizeof(struct coordinate))) == NULL)
		errx(ENOMEM,"out of memory");

	c->x = x;
	c->y = y;

	return (c);
}

void
turn_left(void)
{
	if (direction == SOUTH)
		direction = EAST;
	else
		direction++;
}
