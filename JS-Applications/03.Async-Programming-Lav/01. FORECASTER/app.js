function attachEvents() {
  let weatherButton = document.getElementById("submit");
  let location = document.getElementById("location");
  let currentDiv = document.getElementById("current");
  let upcomingDiv = document.getElementById("upcoming");
  let forecastParentDiv = document.getElementById("forecast");

  const baseUrl = `https://judgetests.firebaseio.com/forecast/`;
  const locationsUrl = `https://judgetests.firebaseio.com/locations.json`;

  const symbols = {
    Sunny: "&#x2600",
    "Partly sunny": "&#x26C5;",
    Overcast: "&#x2601",
    Rain: "&#x2614",
    degrees: "&#176",
  };

  weatherButton.addEventListener("click", () => {
    fetch(locationsUrl)
      .then((response) => response.json())
      .then((data) => {
        let { name, code } = data.find((c) => c.name === location.value);

        //current
        let current = fetch(baseUrl + `today/${code}.json`).then((response) =>
          response.json()
        );

        //upcoming
        let upcoming = fetch(
          baseUrl + `upcoming/${code}.json`
        ).then((response) => response.json());

        Promise.all([current, upcoming])
          .then(showForecast)
          .catch((error) => console.log(error));
      });
  });

  function showCurrent(currentData) {
    let currentSymbol = symbols[currentData.forecast.condition];
    let forecastDiv = createElement("div", "forecasts", "");
    let conditionSymbolSpan = createElement(
      "span",
      "condition symbol",
      currentSymbol
    );
    let conditionInfoSpan = createElement("span", "condition", "");
    let highLow = `${currentData.forecast.low}${symbols.degrees}/${currentData.forecast.high}${symbols.degrees}`;

    let forecastCity = createElement("span", "forecast-data", currentData.name);
    let forecastInfo = createElement("span", "forecast-data", highLow);
    let forecastCondition = createElement(
      "span",
      "forecast-data",
      currentData.forecast.condition
    );

    forecastDiv.appendChild(conditionSymbolSpan);
    currentDiv.appendChild(forecastDiv);
    conditionInfoSpan.appendChild(forecastCity);
    conditionInfoSpan.appendChild(forecastInfo);
    conditionInfoSpan.appendChild(forecastCondition);
    forecastDiv.appendChild(conditionInfoSpan);
  }

  function showUpcoming(upcomingData) {
    let forecastInfo = createElement("div", "forecast-info", "");
    upcomingData.forecast.forEach((obj) => {
      let upcomingSpan = createElement("span", "upcoming", "");
      console.log(obj);
      let conditionSymbol = createElement(
        "span",
        "symbol",
        symbols[obj.condition]
      );
      let highLow = `${obj.low}${symbols.degrees}/${obj.high}${symbols.degrees}`;
      let forecastInfoSpan = createElement("span", "forecast-data", highLow);
      let forecastCondition = createElement(
        "span",
        "forecast-data",
        obj.condition
      );
      upcomingSpan.appendChild(conditionSymbol);
      upcomingSpan.appendChild(forecastInfoSpan);
      upcomingSpan.appendChild(forecastCondition);
      forecastInfo.appendChild(upcomingSpan);
    });
    upcomingDiv.appendChild(forecastInfo);
    console.log(upcomingDiv);
  }

  function showForecast([currentData, upcomingData]) {
    forecastParentDiv.style.display = "block";
    showCurrent(currentData);
    showUpcoming(upcomingData);
  }

  function createElement(element, classes, content = "") {
    let ele = document.createElement(element);
    ele.className = classes;
    ele.innerHTML = content;

    return ele;
  }
}

attachEvents();
