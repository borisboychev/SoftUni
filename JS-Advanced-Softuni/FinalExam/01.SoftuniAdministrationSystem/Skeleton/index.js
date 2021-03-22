function solve() {
  let lectureName = document.querySelector(
    "body > main > section.admin-view.section-view > div > div > form > div:nth-child(1) > input[type=text]"
  );
  let date = document.querySelector(
    "body > main > section.admin-view.section-view > div > div > form > div:nth-child(2) > input[type=datetime-local]"
  );
  let module = document.querySelector(
    "body > main > section.admin-view.section-view > div > div > form > div:nth-child(3) > select"
  );
  let addButton = document.querySelector(
    "body > main > section.admin-view.section-view > div > div > form > div:nth-child(4) > button"
  );

  let userViewModules = document.querySelector(
    "body > main > section.user-view.section-view > div"
  );
  let modulesDiv = document.querySelector(
    "body > main > section.user-view.section-view > div"
  );
  addButton.addEventListener("click", (e) => {
    e.preventDefault();

    //validate inputs
    if (!lectureName.value) {
      return;
    }
    if (module.value === "Select module") {
      return;
    }
    if (!date.value) {
      return;
    }
    let moduleDiv = document.createElement("div");
    moduleDiv.className = "module";

    let moduleH3 = document.createElement("h3");
    moduleH3.innerText = `${module.value.toUpperCase()}-MODULE`;

    let ul = document.createElement("ul");
    let li = document.createElement("li");
    li.className = "flex";

    let h4 = document.createElement("h4");
    let [dateDMY, dateTime] = date.value.split("T");
    dateDMY = dateDMY.replaceAll("-", "/");
    h4.innerText = `${lectureName.value} - ${dateDMY} - ${dateTime}`;

    let deleteButton = document.createElement("buttom");
    deleteButton.className = "red";
    deleteButton.innerText = "Del";

    li.appendChild(h4);
    li.appendChild(deleteButton);

    if (modulesDiv.childNodes.length >= 2) {
      let modulesChildren = modulesDiv.childNodes;

      modulesChildren.forEach(function (node) {
        if (node.childNodes[0].innerText == moduleH3.innerText) {
          node.childNodes[1].appendChild(li);
        }
      });
    }

    ul.appendChild(li);

    moduleDiv.appendChild(moduleH3);
    moduleDiv.appendChild(ul);

    userViewModules.appendChild(moduleDiv);

    deleteButton.addEventListener("click", function (event) {
      //IF MORE THAN ONE LECTURE
      if (
        event.target.parentElement.parentElement.parentElement.parentElement
          .length >= 2
      ) {
        event.target.parentElement.parentElement.remove();
      } else {
        event.target.parentElement.parentElement.parentElement.remove();
      }
    });
  });
}
