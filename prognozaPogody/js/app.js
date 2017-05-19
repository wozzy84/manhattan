window.onload = function () {
  "use strict";

  const canvas = document.getElementById("drawCanvas"); // 500 x 300
  const ctx = canvas.getContext("2d");

  ctx.fillStyle = "rgb(200, 200, 200)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.scale(1, -1);
  ctx.translate(0, -canvas.height);

  const req = new XMLHttpRequest();
  const url = "http://api.openweathermap.org/data/2.5/forecast?q=Warsaw,pl&appid=823afac09c34370d779296d434aea0e9";

  function max(numArray) {
    return Math.max.apply(null, numArray);
  }

  function min(numArray) {
    return Math.min.apply(null, numArray);
  }

  function normalization(max, min) {
    return function (point) {
      return (point - min) / (max - min);
    }
  }

  function fetchSeaLevel(weatherData) { return weatherData.main.sea_level }

  function drawChart(points) {
    ctx.beginPath();
    ctx.strokeStyle = "black";
    ctx.lineWidth = 5;

    ctx.moveTo(0, points[0]);
    points.forEach(function(point, index) {
      ctx.lineTo((canvas.width / points.length) * index, point);
    });
    ctx.stroke();
  }

  function handleData(event) {
    const response = JSON.parse(event.target.response);
    let seaLevels = response.list.map(fetchSeaLevel);
    const maxSeaLevel = max(seaLevels);
    const minSeaLevel = min(seaLevels);

    const normalize = normalization(maxSeaLevel, minSeaLevel);

    seaLevels = seaLevels.map(normalize);
    seaLevels = seaLevels.map(function(seaLevel) { return seaLevel * (canvas.height - 20);});
    drawChart(seaLevels);
  }
  req.addEventListener("load", handleData);
  req.open("GET", url);
  req.send();
}
