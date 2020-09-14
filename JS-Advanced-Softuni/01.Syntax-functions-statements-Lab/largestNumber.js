function solve(nOne, nTwo, nThree) {
  //assume that the first is the biggest
  let biggest = nOne;

  if (nTwo > biggest && nTwo > nThree) {
    biggest = nTwo;
  } else if (nThree > biggest && nThree > nTwo) {
    biggest = nThree;
  }

  console.log(biggest);
}

solve(9, 21, 14);
