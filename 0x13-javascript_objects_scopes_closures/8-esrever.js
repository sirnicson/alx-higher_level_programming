#!/usr/bin/node
/* a function that returns the reversed version of a list */

exports.esrever = function (list) {
  const newArr = [];
  for (let x = list.length - 1; x >= 0; x--) {
    newArr.push(list[x]);
  }
  return (newArr);
};
