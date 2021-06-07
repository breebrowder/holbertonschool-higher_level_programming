#!/usr/bin/node

const Nargs = process.argv;
const argLength = Nargs.length;

argLength < 4 ? console.log(0) : console.log(Nargs.sort()[argLength - 2]);
