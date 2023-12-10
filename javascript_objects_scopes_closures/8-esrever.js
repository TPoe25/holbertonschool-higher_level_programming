#!/usr/bin/node

exports.esrever = function (list) {
  // making a new array with reversed elements
  const reversedList = [];

  // Loopin thru the original list in rev order and puts element to new array
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  // return reversed array
  return reversedList;
};
