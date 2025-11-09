# 🌍 Epidemic Tracker

**Epidemic Tracker** is a full-stack project that visualizes global epidemic-related news and detects potential outbreak clusters using data analysis and machine learning.

---

## 🚀 Overview

This project combines real-time news data, NLP, and geospatial clustering to highlight potential epidemic activity on an interactive world map.

- 🧠 **Backend:** FastAPI (Python) using REST APIs  
- 🗺️ **Frontend:** JavaScript + Leaflet.js  
- 🧩 **Data:** Global news from GDELT API  
- 🗣️ **NLP:** spaCy for geo-entity extraction  
- 📍 **Clustering:** DBSCAN for outbreak detection  

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | FastAPI, SQLAlchemy |
| **Frontend** | JavaScript, Leaflet.js |
| **Data Source** | GDELT API |
| **NLP** | spaCy |
| **Clustering** | Scikit-learn (DBSCAN) |

---

## ⚙️ Quick Start

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/epidemic-tracker.git
cd epidemic-tracker
```

### 2. Run the Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

### 3. Run the Frontend
```bash
cd frontend
npm install
npm run dev
```

Visit: **http://localhost:8080**

---

## 🌐 API Routes

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/locations` | GET | Returns epidemic-related areas and news |
| `/clusters` | GET | Returns DBSCAN cluster results |
| `/user-report` | POST | Submit a user report |

---

## 🗺️ Features

- Real-time epidemic visualization  
- NLP-based location detection  
- DBSCAN clustering for outbreak analysis  
- Interactive world map with hotspots  
- User-submitted news integration  

---
> ⚠️ *For research and visualization only — not a medical prediction tool.*
