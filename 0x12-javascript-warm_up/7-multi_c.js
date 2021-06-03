#!/usr/bin/node

const str = 'C is fun';
const x = process.argv[2];

if (isNaN(parseInt(x))) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < x; i++) {
  console.log(`${str}`);
}
