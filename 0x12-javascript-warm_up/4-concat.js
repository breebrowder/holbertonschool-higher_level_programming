#!/usr/bin/node

const argLength = process.argv.length;
const firstArg = process.argv[2];
const secondArg = process.argv[3];

argLength <= 2 || argLength >= 5 ? console.log('undefined is undefined') : argLength === 3 ? console.log('${firstArg}' + ' is undefined') : console.log('${firstArg}' + ' is ' + '${secondArg}');
