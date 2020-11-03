//Old way of making a request

const url = `https://swapi.dev/api/peoples/`;
let chrElement = document.querySelector(".chr");

const httpReq = new XMLHttpRequest();

//Add Listener
httpReq.addEventListener("loadend", function () {
  let response = JSON.parse(this.responseText);

  if (this.status === 404) {
    chrElement.innerHTML = "<li>No characters</li>";
  }
  let characters = response.results;

  characters.map((x) => {
    let liElement = document.createElement("li");
    liElement.innerText = x.name;
    chrElement.appendChild(liElement);
  });
});

httpReq.open("GET", url);

document.getElementById("load").addEventListener("click", () => httpReq.send());
