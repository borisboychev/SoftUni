function solve(arr) {
  let result = [];
  let max = Number.MIN_SAFE_INTEGER;

  arr.forEach((n) => {
    if (max <= n) {
      max = n;
      console.log(max);
    }
  });
}

solve([1, 3, 8, 4, 10, 12, 3, 2, 24]);
