import './css/index.css';
import { backend_endpoint } from './js/config';

const body = document.querySelector('body');

fetch(backend_endpoint, {
        headers: {
            "ngrok-skip-browser-warning": 1,
        }
    }
).catch((e) => {
    body.innerHTML = '<h1>Server Offline</h1>';
});

