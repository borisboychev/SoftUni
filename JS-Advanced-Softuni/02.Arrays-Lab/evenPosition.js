function solve(arr) {
  let el = "";
  for (let i = 0; i < arr.length; i++) {
    if (i % 2 == 0) {
      el += arr[i] + " ";
    }
  }
  console.log(el.trim());
}

solve([20, 30, 40]);

let a = 12 * 3;
let b = 12 * 3;
