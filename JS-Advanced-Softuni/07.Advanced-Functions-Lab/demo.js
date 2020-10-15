let add = (a, b) => a + b;

function calc(operation, firstOperand, secondOperand) {
  let result = operation(firstOperand, secondOperand);
  return result;
}

console.log(calc(add, 1, 3));
