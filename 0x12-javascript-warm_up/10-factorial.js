#!/usr/bin/node

const numero = parseInt(process.argv[2]);

function factorial (n) {
  return n === 1 || isNaN(n) ? 1 : factorial(n -1) * n;
}
console.log(factorial(numero));
