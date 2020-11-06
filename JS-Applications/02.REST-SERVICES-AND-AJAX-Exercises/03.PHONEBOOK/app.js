function attachEvents() {
  let btnLoad = document.getElementById("btnLoad");
  let btnCreate = document.getElementById("btnCreate");
  //url for get and post requests
  const gpUrl = "https://phonebook-nakov.firebaseio.com/phonebook.json";

  btnLoad.addEventListener("click", () => loadAll(gpUrl));

  btnCreate.addEventListener("click", createObj);

  function loadAll() {
    let phonebook = document.getElementById("phonebook");
    //url for get and post requests

    fetch(gpUrl)
      .then((response) => response.json())
      .then((data) => {
        Object.keys(data).forEach((k) => {
          let liElement = document.createElement("li");
          liElement.textContent = `${data[k].person}: ${data[k].phone}`;

          let delBtn = document.createElement("button");
          delBtn.textContent = "Delete";
          delBtn.addEventListener("click", () => deleteObj(k));

          liElement.appendChild(delBtn);
          phonebook.appendChild(liElement);
        });
      });
  }

  function deleteObj(key) {
    //url for delete request
    const dUrl = `https://phonebook-nakov.firebaseio.com/phonebook/${key}.json`;

    fetch(dUrl, { method: "DELETE" });
  }

  function createObj() {
    let person = document.getElementById("person");
    let phone = document.getElementById("phone");
    let obj = { person: person.value, phone: phone.value };
    obj = JSON.stringify(obj);
    fetch(gpUrl, {
      method: "POST",
      body: obj,
    });
  }
}

attachEvents();
