import { clusters_url } from "./config";

function initializeMap() {
    const map = L.map('map').setView([51.505, -0.09], 5);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    return map;
}

function getClusters() {
    fetch(clusters_url, {
        headers: {
            "ngrok-skip-browser-warning": 1,
        }
    })
    .then((response) => response.json())
    .then((data) => {
        plotClusters(data);
    })
}

function plotClusters(data) {
    for (let val in data) {
        const color = (val === '-1')? "gray": "red";
        for (let coords of data[val]) {
            const circle = L.circleMarker([coords[0], coords[1]], {
            color: color,
            fillColor: color,
            fillOpacity: 0.5,
            radius: 5
        }).addTo(map);
        }
    }
}

const map = initializeMap();
getClusters();