# mediabot_rulaw

# 📊 CSRR Monthly Media Report Bot

Automatically collects **op-eds, print interviews, and TV appearances** from CSRR faculty affiliates every month and saves the results in an Excel file.

---

## 🧑‍💻 Who This Is For

This tool is built for **CSRR fellows and interns** — even if:
- You’ve never coded before
- You don’t have Python or VS Code installed
- You’ve never used the terminal

You’re covered! This guide will walk you through everything.

---

## 🖥️ Setup Instructions

### 🧑‍🍳 Step 1: Install Python and VS Code

#### 🔸 Mac Users

1. **Install Homebrew (helper tool)**  
   Open the **Terminal** and paste this:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**
   ```bash
   brew install python
   ```

3. **Install VS Code**  
   Download from: https://code.visualstudio.com/

---

#### 🔹 Windows Users

1. **Install Python**  
   Download from: https://www.python.org/downloads/  
   ✅ Make sure you check the box: “Add Python to PATH” during installation.

2. **Install VS Code**  
   Download from: https://code.visualstudio.com/

3. **Restart your computer** (helps link everything correctly)

---

## 📁 Step 2: Download and Open the Project

1. Click the green “Code” button on GitHub → then “Download ZIP”.
2. Unzip the file to a folder like `Downloads/CSRR_Monthly_Report_Bot`.
3. Open the folder in VS Code.

---

## 🧪 Step 3: Set Up Your Environment (First Time Only)

1. Open the built-in **terminal** in VS Code:  
   Click “Terminal” → “New Terminal”

2. Create a Python environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the environment:

   - On **Mac**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Step 4: Run the Bot

Make sure your virtual environment is still activated, then run:
```bash
python csrr_google_scraper.py
```

After a few minutes, you’ll see a file called:
```
CSRR_Media_Report.xlsx
```
🎉 That’s your final Excel report!

---

## 🔐 Note About API Keys

This bot uses the **Google Search API (SerpAPI)**.

- You must add your personal API key in the script:
  - Open `csrr_google_scraper.py`
  - Replace `'YOUR_SERPAPI_KEY_HERE'` with your actual key
- To get one: https://serpapi.com/users/sign_up

---

## 🛠 Common Issues

- If `python` isn’t recognized, try using `python3`
- If `pip` fails, try `pip3`
- Restart VS Code if things act weird

---

## 🧼 Want to Start Fresh?

You can delete the following:
```
venv/
__pycache__/
CSRR_Media_Report.xlsx
```

Then re-follow the instructions above. It’ll still work!

