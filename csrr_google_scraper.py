import pandas as pd
import requests
from datetime import datetime, timedelta
import time

SERPAPI_KEY = "3cc26001dcd32f55497a0e787e5683503cea1773bfc612f64629098b54c13592"

# Load names
df = pd.read_csv("csrr_faculty_affiliates_full.csv")
names = df['Name'].tolist()

# 30-day window
today = datetime.today()
start_date = today - timedelta(days=30)

results = []

for name in names:
    query = f'"{name}" op-ed OR interview site:nytimes.com OR site:cnn.com OR site:washingtonpost.com'
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": "10"
    }

    print(f"Searching for: {name}")
    res = requests.get("https://serpapi.com/search", params=params)
    data = res.json()

    organic_results = data.get("organic_results", [])

    for item in organic_results:
        title = item.get("title", "")
        link = item.get("link", "")
        source = item.get("source", "Google")
        snippet = item.get("snippet", "")
        date_str = item.get("date", "")

        # Filter recent results
        if "ago" in date_str or any(str(year) in date_str for year in range(2020, 2026)):
            results.append({
                "Faculty Name": name,
                "Article Title": title,
                "Link": link,
                "Source": source,
                "Publication Date": date_str,
                "Snippet": snippet
            })

    time.sleep(1.5)

# Save results
df_output = pd.DataFrame(results)
df_output.to_excel("CSRR_Media_Report.xlsx", index=False)
print("✅ Done! Saved as CSRR_Media_Report.xlsx")
