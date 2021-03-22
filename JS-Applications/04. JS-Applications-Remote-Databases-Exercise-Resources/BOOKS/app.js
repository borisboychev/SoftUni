const htmlSelectors = {
  loadBooks: () => document.getElementById("loadBooks"),
  createButton: document.querySelector("#createButton > button"),
  createTitleInput: () => document.getElementById("create-title"),
  createAuthorInput: () => document.getElementById("create-author"),
  createIsbnInput: () => document.getElementById("create-isbn"),
  booksContainer: document.querySelector("table > tbody"),
};

htmlSelectors["loadBooks"]().addEventListener("click", fetchAllBooks);

function fetchAllBooks() {
  fetch("https://books-84c38.firebaseio.com/Books/.json")
    .then((res) => res.json())
    .then(renderBooks)
    .catch(handeError);
}

function createDOMelement(type, text, attrs, events, ...children) {
  const domElement = document.createElement(type);

  if (text !== "") {
    domElement.textContent = text;
  }

  Object.entri;
}
