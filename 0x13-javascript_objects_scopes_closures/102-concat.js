#!/usr/bin/node
/* Import the 'fs' module to work with the filesystem */

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

try {
  
  const content1 = fs.readFileSync(file1, 'utf8');
  const content2 = fs.readFileSync(file2, 'utf8');
  
  
  fs.writeFileSync(destination, content1 + content2);

  console.log('Files concatenated successfully!');
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
