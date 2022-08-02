#!/usr/bin/node

const argument = process.argv[2];
const argumentInt = parseInt(argument);
if (isNaN(argumentInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argumentInt);
}
