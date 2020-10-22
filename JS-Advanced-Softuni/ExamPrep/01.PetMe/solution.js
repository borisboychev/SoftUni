function solve() {
  let addButton = document.querySelector("#container > button");
  let inputElements = Array.from(document.querySelectorAll("#container input"));
  let adoptionUl = document.querySelector("#adoption > ul");
  let adoptedUl = document.querySelector("#adopted > ul");

  let [nameElement, ageElement, kindElement, ownerElement] = inputElements;
  addButton.addEventListener("click", (e) => {
    e.preventDefault();

    if (!inputElements.every((x) => x.value)) {
      return;
    }

    //check if age is a number
    if (!Number(ageElement.value)) {
      return;
    }
    console.log("Number");
    let liElement = document.createElement("li");

    //create paragraph element
    let pElement = document.createElement("p");
    pElement.innerHTML = `<strong>${nameElement.value}</strong> is a <strong>${ageElement.value}</strong> year old <strong>${kindElement.value}</strong>`;

    //create span element with owner
    let spanElement = document.createElement("span");
    spanElement.innerText = `Owner: ${ownerElement.value}`;

    //create contact with owner button element
    let buttonElement = document.createElement("button");
    buttonElement.innerText = `Contact with owner`;

    //append all created element to the li
    liElement.appendChild(pElement);
    liElement.appendChild(spanElement);
    liElement.appendChild(buttonElement);

    //append the li to the ul
    adoptionUl.appendChild(liElement);

    nameElement.value = "";
    ageElement.value = "";
    kindElement.value = "";
    ownerElement.value = "";

    buttonElement.addEventListener("click", function (e) {
      e.preventDefault();

      liElement.removeChild(this);
      let takeButtonElement = document.createElement("button");
      takeButtonElement.innerText = "Yes! I take it!";

      let inputElement = document.createElement("input");
      inputElement.placeholder = "Enter your names";

      let divElement = document.createElement("div");

      divElement.appendChild(inputElement);
      divElement.appendChild(takeButtonElement);

      liElement.appendChild(divElement);

      takeButtonElement.addEventListener("click", function (e) {
        e.preventDefault();

        if (inputElement.value === "") {
          return;
        }

        adoptionUl.removeChild(liElement);

        let adopedLiElement = document.createElement("li");

        //pElement.innerHTML = `<strong>${nameElement.value}</strong> is a <strong>${ageElement.value}</strong> year old <strong>${kindElement.value}</strong>`;

        spanElement.innerText = `New Owner: ${inputElement.value}`;

        let checkedButtonElement = document.createElement("button");
        checkedButtonElement.innerText = `Checked`;
        //adoptionUl.removeChild(liElement);

        adopedLiElement.appendChild(pElement);
        adopedLiElement.appendChild(spanElement);
        adopedLiElement.appendChild(checkedButtonElement);

        adoptedUl.appendChild(adopedLiElement);

        checkedButtonElement.addEventListener("click", function (e) {
          e.preventDefault();

          adoptedUl.removeChild(adopedLiElement);
        });
      });
    });
  });
}
