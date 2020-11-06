function getInfo() {
  let stopId = document.getElementById("stopId");
  let stopNameDiv = document.getElementById("stopName");
  let bussesUl = document.getElementById("buses");
  let validBusses = ["1287", "1308", "1327", "2234"];

  if (!validBusses.includes(stopId.value)) {
    stopNameDiv.textContent = "Error";
    return;
  }
  const url = `https://judgetests.firebaseio.com/businfo/${stopId.value}.json`;

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      stopNameDiv.textContent = data.name;
      Object.keys(data.buses).forEach(
        (b) =>
          (bussesUl.innerHTML += `<li>Bus ${b} arrives in ${data.buses[b]} minutes</li>`)
      );
    });
}
