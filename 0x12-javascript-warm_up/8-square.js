#!/usr/bin/node

const x = process.argv[2];

if (isNaN(parseInt(x)) || x <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
