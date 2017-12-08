const input = 265149

function manhattan(input) {
	let n=0, last=1, num, radius, manhattan;

	// find which two "radial numbers" the input is in between
	while (++n) {
		if (n%4 < 2) {
			num = n * (n+3) / 4 + 1
		} else {
			num = (n+1) * (n+2) / 4 + 1
		}
		if (num >= input)
			break;
		last = num;
	}

	if ((input - last) < (num - input)) {
		// if we're closer to the lower number, use that
		radius = Math.ceil((n-1)/4);
		manhattan = radius + (input - last)
	} else {
		// otherwise we're closer to the higher number
		radius = Math.ceil(n/4);
		manhattan = radius + (num - input)	
	}

	console.log(manhattan);
}

manhattan(input);