# 📊 CSRR Monthly Media Report Bot

This project automates the process of generating a monthly media report for faculty affiliated with the Rutgers Center for Security, Race and Rights (CSRR). It uses the Google Search API (via SerpAPI) to scrape articles, interviews, and mentions of CSRR faculty and compiles the results into an Excel file.

---

## 🚀 Features

- Searches Google News for each CSRR faculty member
- Filters relevant results based on publication date
- Extracts key information:
  - Faculty name
  - Article title
  - Source
  - Date
  - Snippet
  - Link
- Outputs to a formatted Excel file: `CSRR_Media_Report.xlsx`

---

## 🧱 Requirements

- Python 3.8 or later (tested on 3.13)
- SerpAPI key (free tier available)
- macOS (works best with ARM-based Macs, e.g. M1/M2/M3)

---

## 📦 Installation & Setup

### 1. Clone or download this repository.

### 2. Run the one-click setup script:
```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Create a virtual environment
- Install required packages: `pandas`, `openpyxl`, and `serpapi`
- Prompt you to add your API key

---

## 🔑 SerpAPI Key Setup

To run the scraper, you need a SerpAPI key:

1. Go to [https://serpapi.com/](https://serpapi.com/) and sign up.
2. Copy your API key.
3. Open the file `csrr_google_scraper.py` and paste your key:
```python
params = {
  "q": f"{name} site:news.google.com",
  "api_key": "YOUR_API_KEY_HERE",
  ...
}
```

---

## 🧪 Run the Bot

Once setup is complete, run the script:

```bash
python3 csrr_google_scraper.py
```

You’ll see each faculty name printed as it’s searched. Once complete, your Excel report will appear as:

```
✅ Done! Saved as CSRR_Media_Report.xlsx
```

---

## 📁 Output

- File: `CSRR_Media_Report.xlsx`
- Format: One row per news article
- Columns: Faculty Name, Article Title, Link, Source, Publication Date, Snippet

---

## 🤝 Credits

Created by Azra Bano  
In collaboration with Rutgers Center for Security, Race and Rights (CSRR)

---

## 🧼 Optional Cleanup

To remove the virtual environment:

```bash
deactivate
rm -rf venv
```

---

## 🛠️ Future Improvements

- Filter by date range (e.g. current month only)
- Add support for print/TV appearance detection
- Deploy to a server for scheduled auto-runs
