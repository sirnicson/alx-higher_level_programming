#!/usr/bin/node
/* prints a message based on no of arguments passed */
const args = process.argv;

if (args.length <= 2) {
	console.log('No Argument');
} else if (args.length === 3) {
	console.log('Argument found');
} else {
	console.log('Argument found');
}
