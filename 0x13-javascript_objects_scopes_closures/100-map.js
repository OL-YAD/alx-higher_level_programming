#!/usr/bin/node
const list = require('./100-data');
let counter = 0;
console.log(list.list);
console.log(list.list.map(x => x * counter++));
