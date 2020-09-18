function solve(arr) {
  let count = arr.pop();
  for (let i = 0; i < count % arr.length; i++) {
    arr.unshift(arr.pop());
  }
  console.log(arr.join(" "));
}

solve(["1", "2", "3", "4", "2"]);
