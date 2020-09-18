function solve(arr) {
  let step = Number(arr.pop());

  // arr.forEach(function (v, i) {
  //   if (i % step == 0) {
  //     console.log(v);
  //   }
  // });

  for (let i = 0; i < arr.length; i += step) {
    console.log(arr[i]);
  }
}

solve(["5", "20", "31", "4", "20", "2"]);
