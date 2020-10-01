function addItem() {
  let inputElement = document.getElementById("newItemText");
  let liElement = document.createElement("li");
  let itemListElement = document.getElementById("items");
  liElement.innerHTML = inputElement.value;

  itemListElement.appendChild(liElement);

  inputElement.value = "";
}
