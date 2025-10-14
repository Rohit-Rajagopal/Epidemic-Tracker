import { add_news_url } from "./config";

document.getElementById("newsForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const area = document.getElementById("area").value;
    const country = document.getElementById("country").value;
    const title = document.getElementById("title").value;
    const url = document.getElementById("url").value || "";

    const payload = {
        "area": area,
        "country": country,
        "news": title,
        "url": url
    };

    const responseMsg = document.getElementById("responseMsg");

    try {
        const response = await fetch(add_news_url, { // change URL to your API
            method: "POST",
            headers: { 
                "ngrok-skip-browser-warning": 1,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            responseMsg.style.color = "green";
            responseMsg.textContent = "News report submitted successfully!";
            document.getElementById("newsForm").reset();
        } else {
            responseMsg.style.color = "red";
            responseMsg.textContent = "Failed to submit news report.";
        }
    } catch (error) {
        responseMsg.style.color = "red";
        responseMsg.textContent = "Error: Could not connect to server.";
        console.error(error);
    }
});
