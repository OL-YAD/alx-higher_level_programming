#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  if (dict[key] in newDict) {
    newDict[dict[key]] = newDict[dict[key]].concat([key]);
  } else {
    newDict[dict[key]] = [key];
  }
}
console.log(newDict);
