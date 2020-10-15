function solve() {
  let boxEl = document.getElementById("box");

  boxEl.addEventListener("click", function (e) {
    console.log(this === boxEl);
  });
}
