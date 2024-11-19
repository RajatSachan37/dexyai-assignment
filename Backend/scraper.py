from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor
import time

from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

company_data = {
    "Microsoft": {
        "url": "https://www.microsoft.com/en-us/about",
        "xpath": '/html/body/div[3]/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]'
    },

    "Google": {
        "url": "https://about.google/intl/ALL_in",
        "xpath": '/html/body/main/div/section[1]/div/div[2]/h1'
    },
    "Amazon": {
        "url": "https://www.aboutamazon.com/about-us",
        "xpath": '/html/body/section/div[2]/div/div[1]/p/span'
    },
    "Meta": {
        "url": "https://about.meta.com/",
        "xpath": '/html/body/div/div/div[4]/div[3]/div[3]/div/div/h1'
    },
    "Samsung": {
        "url": "https://www.samsung.com/us/about-us/our-business",
        "xpath": '/html/body/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/h2'
    },
    "Accenture": {
        "url": "https://www.accenture.com/in-en/about/company-index",
        "xpath": '/html/body/div[2]/main/div/div[3]/div/div[1]/h3'
    },
    "Capgemini": {
        "url": "https://www.capgemini.com/in-en/about-us/",
        "xpath": '/html/body/div[7]/section/section[1]/div/div/div/div[2]/p'
    },
    "SAP": {
        "url": "https://www.sap.com/india/about/company.html",
        "xpath": '/html/body/div[3]/main/section/div[4]/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]'
    },
    "AMD": {
        "url": "https://www.amd.com/en/corporate.html",
        "xpath": '/html/body/div[8]/div/div/div/div/div[3]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/p[1]'
    },
    "Cisco": {
        "url": "https://www.cisco.com/c/en/us/about.html",
        "xpath": '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/p'
    },

    

    
    
    
}

def scrape_company(company_name, company_info):
    url = company_info["url"]

    xpath = company_info["xpath"]

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)
        try:
            result = driver.find_element(By.XPATH, xpath)
            if result:
                return {"company": company_name, "url": url, "data": result.text.strip()}
            else:
                return {"company": company_name, "url": url, "error": "Data not found for the given selector"}
        except Exception as e:
            return {"company": company_name, "url": url, "error": f"Element not found: {str(e)}"}

    except Exception as e:
        return {"company": company_name, "url": url, "error": f"Request error: {str(e)}"}

    finally:
        driver.quit()


@app.route("/scrape", methods=["GET"])
def scrape_data():
    try:
        results = []
        with ThreadPoolExecutor() as executor:
            results = executor.map(
                lambda item: scrape_company(item[0], item[1]),
                company_data.items()
            )
        return jsonify({"data": list(results)})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run()
