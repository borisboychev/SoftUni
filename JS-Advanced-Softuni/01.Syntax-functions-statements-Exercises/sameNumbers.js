function solve(n) {
  let sum = 0;
  let isSame = true;
  for (let i = 0; i < String(n).length; i++) {
    number = String(n)[i];
    if (i > 0 && number != String(n)[i - 1]) {
      isSame = false;
    }
    sum += Number(number);
  }
  console.log(isSame);
  console.log(sum);
}

solve(2422);
