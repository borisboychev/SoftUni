function solve(arr) {
  let maxNum = arr.map((row) => Math.max(...row));
  console.log(maxNum.sort((a, b) => a - b).reverse()[0]);
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
