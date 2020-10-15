function solve(coords) {
  let board = [
    [false, false, false],
    [false, false, false],
    [false, false, false],
  ];

  let player = "X";
  coords.forEach((line) => {
    let [r, c] = line.split(" ").map((n) => Number(n));
    if (!board[r][c]) {
      board[r][c] = player;
    } else {
      console.log("This place is already taken. Please choose another!");
      continue;
    }
    player = player === "X" ? "O" : "X";
  });
  console.log(board.join(""));
}

solve(["0 1", "0 0", "0 2", "2 0", "1 0", "1 1", "1 2", "2 2", "2 1", "0 0"]);
