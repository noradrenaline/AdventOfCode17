let banks = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4];
const num_banks = banks.length;
let previous_states = {};

function banks_to_string() {
	return banks.join('|');
}

function cycle() {
	const biggest = get_max();
	const num_blocks = banks[biggest];
	let i;

	// redistribute blocks
	banks[biggest] = 0;

	banks = banks.map(x => x + Math.floor(num_blocks / num_banks));

	for (i=1; i <= (num_blocks % num_banks); i++) {
		banks[(biggest + i) % num_banks]++;
	}
}

function get_max() {
	let max = 0;
	let ix = -1;
	banks.forEach((b, i) => {
		if (b > max) {
			max = b
			ix = i;
		}
	})
	return ix;
}

function run() {
	let found = false;
	let count = 0;
	while (++count) {
		previous_states[banks_to_string()] = true;
		cycle();
console.log(banks_to_string());

		if (previous_states[banks_to_string()]) {
			if (!found) {
				found = true;
				count = 0;
				previous_states = {};
				previous_states[banks_to_string()] = true;
			} else {
				break;
			}
		}
	}

	return count;
}

console.log(run());