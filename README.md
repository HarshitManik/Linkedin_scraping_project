# 🔍 LinkedIn Scraping Project

A Python-based LinkedIn scraping automation tool designed to extract profile details based on specific search keywords, with optional integration to personalize and automate connection requests. Built for recruitment analysis, networking, and lead generation purposes.

---

## 🚀 Features

- 🔑 Keyword-based profile scraping (e.g., "HR at Google", "Data Scientist Bangalore")
- 🌐 Browser automation using **Selenium** or **Playwright**
- 📥 Extracts name, headline, current company, location, profile link, etc.
- 📄 Stores data into a structured **CSV/Excel file**
- ✉️ (Optional) Personalized connection message automation
- 🧠 Modular design for integration with agent-based frameworks like **CrewAI**

---

## 📁 Project Structure

Linkedin_scraping_project/
│
├── src/
│ ├── linkedin_scraper.py # Core scraping logic
│ ├── connection_requester.py # (Optional) Sends automated requests
│ ├── utils.py # Helper functions
│
├── data/
│ └── output.csv # Scraped data stored here
│
├── config/
│ └── settings.yaml # Configuration for keywords, browser options, delays
│
├── README.md # You're here!
├── requirements.txt # Python dependencies
└── .gitignore # To avoid pushing credentials or local browser data

yaml
Copy code

---

## ⚙️ Technologies Used

- **Python 3.x**
- **Selenium / Playwright** (choose one)
- **Pandas** – data formatting
- **OpenPyXL / CSV** – export support
- **YAML** – configuration
- **CrewAI (optional)** – for modular agent-based task handling

---

## 🧑‍💻 How to Run

### 1. Clone the Repository

bash
git clone https://github.com/HarshitManik/Linkedin_scraping_project.git
cd Linkedin_scraping_project
2. Setup a Virtual Environment (Recommended)
bash
Copy code
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.\.venv\Scripts\activate    # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Add your LinkedIn Credentials (Securely)
Update the config/settings.yaml file with:

yaml
Copy code
linkedin_email: "your-email@example.com"
linkedin_password: "your-password"
search_keywords:
  - "HR at Microsoft"
  - "Talent Acquisition Google"
✅ For secure setups, use environment variables or a .env file.

5. Run the Scraper
bash
Copy code
python src/linkedin_scraper.py
📊 Output Example
Example data saved to data/output.csv:

Name	Headline	Company	Location	Profile Link
John Doe	HR Manager at Microsoft	Microsoft	Seattle, WA	https://linkedin.com/in/johndoe
Priya Sharma	Talent Acquisition @Google	Google	Bengaluru	https://linkedin.com/in/priyasharma

📌 TODO / Future Work
 Add headless mode for background scraping

 Integrate OpenAI API to summarize profiles

 Add retry logic and scraping delay for LinkedIn bans

 GUI-based keyword and result selection

 CrewAI Agent Integration for modular scraping + messaging

⚠️ Disclaimer
This tool is intended for educational and research purposes only. Scraping LinkedIn may violate their Terms of Service. Use responsibly and at your own risk.

🧠 Author
Harshit Manik

GitHub: @HarshitManik

Email: harshitmanik@gmail.com (or update to preferred contact)

⭐️ Support
If you find this project useful, give it a ⭐️ on GitHub and share it with others!

yaml
Copy code

---

Let me know if you’d like to:

- Add **screenshots or demo videos**
- Include an **API wrapper**
- Connect with MongoDB, CrewAI, or deploy with FastAPI

Happy scraping! 🕵️‍♂️
