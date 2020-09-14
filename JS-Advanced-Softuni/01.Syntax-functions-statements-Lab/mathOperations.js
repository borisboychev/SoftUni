function solve(numOne, numTwo, operator) {
  switch (operator) {
    case "+":
      console.log(numOne + numTwo);
      break;
    case "-":
      console.log(numOne - numTwo);
      break;
    case "*":
      console.log(numOne * numTwo);
      break;
    case "/":
      console.log(numOne / numTwo);
      break;
    case "%":
      console.log(numOne % numTwo);
      break;
    case "**":
      console.log(Math.pow(numOne, numTwo));
      // x ** y
      break;
  }
}

solve(2, 2, "**"); // 4
solve(2, 5, "*"); // 10
solve(4, 2, "/"); // 2
solve(3, 2, "%"); // 1
solve(3, 3, "+"); // 6
solve(2, 2, "-"); // 0
