const input = 265149

const directions = [{'x': 0, 'y': -1}, {'x': 1, 'y': 0}, {'x': 0, 'y': 1}, {'x': -1, 'y': 0}];
const surrounding = [{'x': 0, 'y': -1}, {'x': 1, 'y': 0}, {'x': 0, 'y': 1}, {'x': -1, 'y': 0}, {'x': 1, 'y': -1}, {'x': 1, 'y': 1}, {'x': -1, 'y': 1}, {'x': -1, 'y': -1}];

let plane = []
let direction = 0;
let value = 0;
let coordinates = {'x': 0, 'y': 0};

function initialize() {
	plane[0] = [];
	plane[0][0] = 1;
}

function is_set(coordinates) {
	return !(plane[coordinates.x] === undefined || plane[coordinates.x][coordinates.y] === undefined)
}

function move(coordinates, direction) {
	let x = coordinates.x + 1*direction.x;
	let y = coordinates.y + 1*direction.y;
	return {'x': x, 'y': y};
}

function get_value(coordinates) {
	if (plane[coordinates.x] === undefined) plane[coordinates.x] = [];
	return plane[coordinates.x][coordinates.y];
}

function set_value(coordinates, value) {
	if (plane[coordinates.x] === undefined) plane[coordinates.x] = [];
	plane[coordinates.x][coordinates.y] = value;
}

function sum_surrounding(coordinates) {
	let sum = 0;
	surrounding.forEach((direction) => {
		const value = get_value(move(coordinates, direction));
		sum += (value !== undefined) ? value : 0;
	});
	return sum;
}

function walk() {
	// can we change directions?
	let next_direction = (direction + 1) % 4;
	let next_step = move(coordinates, directions[next_direction])
	if (is_set(next_step)) {
		next_step = move(coordinates, directions[direction])
	} else {
		direction = next_direction;
	}
	coordinates = next_step;
	let value = sum_surrounding(coordinates);
	set_value(coordinates, value);
	return value;
}

initialize();

let c = 0;
while (++c < 1000) {
	value = walk();
	if (value > input)
		break;
}

console.log(value);