# Amazon Product Scraper – Streamlit Web App

After successfully completing the code for scraping Amazon products, I wanted to take the challenge even further.

This is a Streamlit Web Application that allows the user to simply enter a URL, and then with a slider choose the number of pages to scrap.

For example, if you search for "coffee machines" on Amazon.fr, the results might span over 7 pages of different machines. With this app, you can choose how many pages you want to scrape.

---

## How It Works

### Step 1: Enter the URL  
Paste the Amazon.fr search page URL into the input field.

### Step 2: Select Number of Pages  
Use the slider to choose how many pages of products you'd like to scrape.

### Step 3: Submit the Form  
Click the **Submit** button to scrape the links. Once it's done, it will show you how many products were found.  
Then you'll move to the second part.

### Step 4: Choose a File Name  
In the second section, type a name for your CSV file (for example: `coffee_machines`).

### Step 5: Wait a Few Moments  
It may take a few minutes depending on the number of pages selected.

### Step 6: Download the CSV File  
A download button will appear. Click it to download a ready-to-analyze CSV file containing:
- Product title  
- Product price  
- Product link  
- Scraping date  

---

## Notes

- This project is made for educational and personal use only.
- Built with Streamlit, BeautifulSoup, requests, and csv.
- Make sure to follow Amazon's Terms of Service when using this tool.

---

## Files

- `Web_app.py` – Main Streamlit app
- `backend.py` – Scraping functions
- `requirements.txt` – Python dependencies

---

## Author

Created by Abderraouf Rahmani – always trying to go a step further.
