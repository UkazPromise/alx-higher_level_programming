#!/usr/bin/node

const firstArg = process.argv[2];

const integerValue = parseInt(firstArg);

if (!isNaN(integerValue)) {
    console.log('My number:', integerValue);
} else {
    console.log('Not a number');
}
