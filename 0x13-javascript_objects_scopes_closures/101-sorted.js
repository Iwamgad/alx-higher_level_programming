#!/usr/bin/node

const dict = require('./101-data').dict;
const ret = {};
for (const item in dict) {
    if (!(dict[item] in ret)) {
        ret[dict[item]] = [item];
    } else {
        ret[dict[item]].push(item);
    }
}
console.log(ret);
