//New way of making a request

const url = `https://swapi.dev/api/people/`;

//To catch an exepction
// const url = `https://swapi.dev/api/people/`;

let chrElement = document.querySelector(".chr");

document.getElementById("load").addEventListener("click", () => {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      let characters = data.results;

      characters.map((x) => {
        let liElement = document.createElement("li");
        liElement.innerText = x.name;
        chrElement.appendChild(liElement);
      });
    })
    .catch((error) => {
      let liElement = document.createElement("li");
      liElement.innerText = "No characters";
      chrElement.appendChild(liElement);
    });
});
