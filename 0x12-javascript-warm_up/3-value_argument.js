#!/usr/bin/node

// Check if an argument is provided
if (process.argv[2] !== undefined) {
    console.log(process.argv[2]);
} else {
    console.log("No argument");
}
