#!/usr/bin/node
/* prints "My number:x" if the first argument is integer convertible */

const args = process.argv[2];

if (args === undefined || isNaN(parseInt(args))) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + parseInt(args));
}
