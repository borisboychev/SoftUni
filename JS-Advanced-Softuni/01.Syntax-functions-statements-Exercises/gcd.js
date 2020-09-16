function solve(one, two) {
  bigger = Math.max(one, two);
  smaller = Math.min(one, two);

  for (let i = smaller; i >= 0; i--) {
    if (bigger % i == 0 && smaller % i == 0) {
      console.log(i);
      break;
    }
  }
}

// solve(3768, 1701);
solve(15, 5);
// solve(2154, 458);
