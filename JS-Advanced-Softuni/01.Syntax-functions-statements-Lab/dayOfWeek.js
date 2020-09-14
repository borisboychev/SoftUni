function solve(day) {
  let result;
  switch (day) {
    case "Monday":
      result = 1;
      break;
    case "Tuesday":
      result = 2;
      break;
    case "Wednesday":
      result = 3;
      break;
    case "Thursday":
      result = 4;
      break;
    case "Friday":
      result = 5;
      break;
    case "Saturday":
      result = 6;
      break;
    case "Sunday":
      result = 7;
      break;
  }

  if (typeof result == "undefined") {
    throw "error";
  } else {
    console.log(result);
  }
}

solve("Monday"); // prints 1
//solve("asasas"); // throws error
