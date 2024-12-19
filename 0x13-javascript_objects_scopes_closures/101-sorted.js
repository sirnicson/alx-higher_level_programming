#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user id */

const dic = require('./101-data.js').dict;
const newDic = {};
for (const key in dic) {
  if (newDic[dic[key]]) newDic[dic[key]].push(key);
  else newDic[dic[key]] = [key];
}
console.log(newDic);
