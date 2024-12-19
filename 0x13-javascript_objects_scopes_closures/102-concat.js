#!/usr/bin/node
/* Import the 'fs' module to work with the filesystem */

const fs = require('fs');

const [source1, source2, destination] = process.argv.slice(2);

const content1 = fs.readFileSync(source1, 'utf8');
const content2 = fs.readFileSync(source2, 'utf8');

fs.writeFileSync(destination, content1 + content2);
