#!/usr/bin/node

function factorial (number) {
  if (number === 1 || isNaN(number)) {
    return 1;
  }
  return (number * factorial(number - 1));
}
const argument = process.argv[2];
const fact = factorial(parseInt(argument));
console.log(fact);
