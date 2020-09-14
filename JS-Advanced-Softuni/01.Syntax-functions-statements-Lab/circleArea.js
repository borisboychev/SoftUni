function solve(x) {
  let type = typeof x;
  let result;
  if (type === "string") {
    result = `We can not calculate the circle area, because we recieved a ${type}`;
  } else {
    result = (x ** 2 * Math.PI).toFixed(2);
  }

  console.log(result);
}

solve(5);
