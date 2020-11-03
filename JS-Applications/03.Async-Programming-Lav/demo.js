// Callbacks
function running() {
  return "running";
}

function category(run, type) {
  console.log(run() + " " + type);
}

category(running, "sprint");

console.log("---------------------");

// Promise
let promise = new Promise((resolve, reject) => {
  console.log("Prepare promise");
  if (something) {
    resolve();
  } else if (somethingElse) {
    reject();
  }
});
