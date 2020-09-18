function solve(commands) {
  let arr = [];

  commands.forEach((command, i) => {
    command == "add" ? arr.push((i += 1)) : arr.pop();
  });
  arr.length == 0 ? console.log("Empty") : arr.forEach((el) => console.log(el));
}

solve(["remove", "add", "add"]);
