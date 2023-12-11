#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // filter method to make an array of elements like searchElement
  const occurences = list.filter(element => element === searchElement);

  // Return the length of occurences
  return occurences.length;
};
