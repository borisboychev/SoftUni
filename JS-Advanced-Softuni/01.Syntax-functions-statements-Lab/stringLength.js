function solve(arrOne, arrTwo, arrThree) {
  let averageLength = Math.floor(
    (arrOne.length + arrTwo.length + arrThree.length) / 3
  );
  let sumLength = arrOne.length + arrTwo.length + arrThree.length;

  console.log(sumLength);
  console.log(averageLength);
}

solve("chocolate", "ice cream", "cake");
