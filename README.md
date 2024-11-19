# Company Info Scraper

A web application to scrape company information from specific websites using a Flask backend and a React frontend. This project demonstrates how to use web scraping with Selenium and display the results dynamically in a user-friendly table format.

---

## Features

- Scrape company information from predefined websites using XPath.
- Display scraped data in a responsive and styled table using React Bootstrap.
- Error handling for failed requests or scraping issues.
- Dynamic status messages for loading, errors, and successful data fetches.

---

## Technologies Used

### Backend:
- **Flask**: For creating the backend API.
- **Selenium**: For web scraping using browser automation.

### Frontend:
- **React**: For building the interactive user interface.
- **Axios**: For making HTTP requests to the backend.
- **React Bootstrap**: For styling the components.

---

## Prerequisites

1. Install **Python 3.7+** on your system.
2. Install **Node.js** and **npm**.
3. Install **Google Chrome**.
4. Download **ChromeDriver** compatible with your Chrome version from.

---

## Steps to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/RajatSachan37/dexyai-assignment.git
cd dexyai-assignment
```
### 2. Navigate to the Backend folder:
```bash
cd Backend
```
### 3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 5. Run the Flask server:
```bash
python scraper.py
```
By default, the server will run at:
```bash
 http://127.0.0.1:5000/scrape
```
### 6. Navigate to the Frontend folder:
```bash
cd ../Frontend
```
### 7. Install dependencies:
```bash
npm install
```
### 8. Start the React development server:
```bash
npm start
```
By default, the React app will run at:
```bash
http://localhost:3000
```
