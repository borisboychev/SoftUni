function solve(arr) {
  let towns = {};
  for (let i = 0; i < arr.length; i += 2) {
    if (towns[arr[i]]) {
      towns[arr[i]] += Number(arr[i + 1]);
    } else {
      towns[arr[i]] = Number(arr[i + 1]);
    }
  }
  console.log(towns);
}

solve(["Sofia", 20, "Varna", 10, "Sofia", 5, "Lovech", 1212]);
