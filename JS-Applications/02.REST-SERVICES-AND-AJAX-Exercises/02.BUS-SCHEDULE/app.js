function solve() {
  let departButton = document.getElementById("depart");
  let arriveButton = document.getElementById("arrive");
  let info = document.getElementById("info");
  let stopId = "depot";
  let stopName;
  const baseUrl = `https://judgetests.firebaseio.com/schedule/`;

  function changeButton() {
    if (departButton.disabled) {
      departButton.disabled = false;
      arriveButton.disabled = true;
    } else {
      departButton.disabled = true;
      arriveButton.disabled = false;
    }
  }

  function depart() {
    const url = `${baseUrl}${stopId}.json`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        info.textContent = "Next stop " + data.name;
        stopId = data.next;
        stopName = data.name;
      })
      .catch(() => {
        info.textContent = "ERROR";
      });

    changeButton();
  }

  function arrive() {
    info.textContent = "Arriving at " + stopName;
    changeButton();
  }

  return {
    depart,
    arrive,
  };
}

let result = solve();
