import { locations_url } from "./config";

const dialog = document.querySelector("dialog");
const dialogName = dialog.querySelector('p.name');
const dialogEntries = dialog.querySelector('.entries');

class Area {
    constructor(data) {
        this.name = data['area'];
        this.coords = data['coordinates'];
        this.entries = data['entries'];
    }
}

function initializeMap() {
    const map = L.map('map').setView([51.505, -0.09], 5);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    return map;
}

function addCircles(data) {
    for (let area of data) {
        let coords = area.coords
        const circle = L.circleMarker([coords[0], coords[1]], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: 5
        }).addTo(map);
        circle.obj = area
        circle.on('click', (e) => {
            dialogName.textContent = e.target.obj.name;
            const ol = document.createElement("ol");
            for (let entry of e.target.obj.entries) {
                const li = document.createElement("li");
                const a = document.createElement("a");
                a.textContent = entry["title"];
                a.href = entry["url"];
                li.appendChild(a)
                ol.appendChild(li)
            }
            dialogEntries.innerHTML = '';
            dialogEntries.appendChild(ol);
            dialog.showModal();
        })
    }
}


function createAreas(data) {
    const allAreas = [];
    for (let area of data['areas']) {
        const newArea = new Area(area);
        allAreas.push(newArea);
    }
    return allAreas;
}

function getAreas() {
    fetch(locations_url, {
        headers: {
            "ngrok-skip-browser-warning": 1,
        }
    })
    .then((response) => response.json())
    .then((data) => {
        addCircles(createAreas(data))
    })
}


const map = initializeMap();
getAreas();