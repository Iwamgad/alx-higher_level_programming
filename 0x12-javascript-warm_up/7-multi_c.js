#!/usr/bin/node
const c = process.argv[2];
if (isNaN(c)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < c; i++) {
        console.log('C is fun');
    }
}
