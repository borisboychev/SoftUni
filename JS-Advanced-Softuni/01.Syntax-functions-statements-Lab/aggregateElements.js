function sum(numbers) {
  let result = 0;
  numbers.forEach(function (number) {
    result += number;
  });
  return result;
}

function sumInverse(numbers) {
  let result;
  let inverseNumbers = [];

  numbers.forEach(function (number) {
    inverseNumbers.push(1 / number);
  });
  result = sum(inverseNumbers);
  return result.toFixed(4);
}

function concat(numbers) {
  let result = "";

  numbers.forEach(function (number) {
    result += number;
  });

  return result;
}

console.log(sum([1, 2, 3]));
console.log(sumInverse([1, 2, 3]));
console.log(concat([1, 2, 3]));
