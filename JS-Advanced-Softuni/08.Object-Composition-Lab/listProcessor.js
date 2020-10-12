function solve(input) {
  let result = [];
  input.map((el) => {
    let [command, string] = el.split(" ");
    switch (command) {
      case "add":
        result.push(string);
        break;
      case "remove":
        result = result.filter((el) => el != string);
        break;
      case "print":
        console.log(result.join(", "));
        break;
    }
  });
}

solve(["add hello", "add again", "remove hello", "add again", "print"]);
solve(["add pesho", "add george", "add peter", "remove peter", "print"]);
