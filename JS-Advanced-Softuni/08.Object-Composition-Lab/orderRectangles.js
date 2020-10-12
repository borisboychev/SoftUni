function solve(input) {
  let result = input.map(([width, height]) => {
    return {
      width: width,
      height: height,
      area() {
        return this.width * this.height;
      },
      //positive number if the current rect is bigger
      compareTo(rect) {
        return this.area() - rect.area();
      },
    };
  });
  result.sort((a, b) => {
    return b.compareTo(a);
  });
  console.log(result);
}

solve([
  [10, 5],
  [5, 12],
]);
