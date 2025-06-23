#!/bin/bash

echo "🚀 Setting up CSRR Media Report Bot..."

# Step 1: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 2: Upgrade pip
pip install --upgrade pip

# Step 3: Install dependencies
pip install pandas serpapi openpyxl

# Step 4: Run the scraper
python3 csrr_google_scraper.py

# Step 5: Notify user
echo "✅ Done! Check the CSRR_Media_Report.xlsx file."

# Optional: Keep the environment activated
$SHELL
