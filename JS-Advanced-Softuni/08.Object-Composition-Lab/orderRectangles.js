function solve(input) {
  let result = input.map(([width, height]) => {
    return {
      width: width,
      height: height,
      area() {
        return this.width * this.height;
      },
      compareTo(rect) {
        return this.area() - rect.area();
      },
    };
  });
  let first = result[0];
  let second = result[1];

  console.log(first.compareTo(second));
}

solve([
  [10, 5],
  [5, 12],
]);
