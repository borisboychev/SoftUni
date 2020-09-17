function solve(arr) {
  let result = [];
  for (const array of arr) {
    array.sort((a, b) => a - b).reverse();
    result.push(array[0]);
  }
  result.sort((a, b) => a - b).reverse();
  console.log(result[0]);
}

// solve([
//   [20, 50, 10],
//   [8, 33, 145],
// ]);

solve([
  [3, 5, 7, 12],
  [-1, 4, 33, 2],
  [8, 3, 0, 4],
]);
