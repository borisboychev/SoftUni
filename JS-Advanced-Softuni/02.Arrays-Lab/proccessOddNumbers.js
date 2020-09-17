function solve(numbers) {
  let res = numbers.filter((x, i) => i % 2 != 0).map((x) => x * 2);
  let reversed = res.reverse();
  console.log(reversed.join(" "));
}

solve([10, 15, 20, 25]);
