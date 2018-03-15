var wsaddr = window.location.host;
var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
var path = window.location.pathname.replace(/\/$/, "");
var wsUri = ws_scheme + "://" + wsaddr + path + "/ws/";
var websocket;


function setupWebSocket() {
  websocket = new WebSocket(wsUri);
  websocket.onopen = function(evt) { onOpen(evt) };
  websocket.onmessage = function(evt) { onMessage(evt) };
}

function onOpen (evt) {
  console.log("Connected to websocket!");
  websocket.send(JSON.stringify({
  		contest:document.getElementById('con_name').innerHTML
  }))
}

function onMessage (evt) {
  var Html = document.getElementById("discuss").innerHTML;
  document.getElementById("discuss").innerHTML = evt.data+ Html;
}
