function solve(arr) {
  let result = [];
  for (const number of arr) {
    if (number >= 0) {
      result.push(number);
    } else {
      result.unshift(number);
    }
  }
  console.log(result);
}

solve([7, -2, 8, 9]);
