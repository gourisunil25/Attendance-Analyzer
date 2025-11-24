# Flask Attendance Analyzer 📊

**A simple, clean tool to visualize attendance stats.**

I built this project because reading raw CSV files is tedious. This app takes your attendance data, calculates the percentages for you, and presents it in a modern, minimalist dashboard.

## 🚀 Features

* **Instant Analysis:** Upload a CSV and get subject-wise breakdowns immediately.
* **Visuals:** Generates Bar and Pie charts automatically using Matplotlib.
* **Flexible Input:** Works with three different CSV formats (see below).
* **Responsive UI:** Uses a custom CSS grid layout that looks good on desktop and mobile.

## 🛠️ How to Run Locally

This is a standard Flask app. I recommend using a virtual environment

**1. Clone and Setup**
```bash
git clone [https://github.com/yourusername/attendance-analyzer.git](https://github.com/yourusername/attendance-analyzer.git)
cd attendance-analyzer

## How to run
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000` and upload a CSV.

## CSV formats supported
1. **Per-subject summary** with columns: `Subject,Attended,Total`  
2. **Per-class rows** with columns: `Subject,Present` (Present=1 if attended else 0)  
3. **Per-student with Present** columns: `Student,Present` (will give per-student %)

## 🏗️ Project Structure
attendance-analyzer/
├── app.py              # Main Flask application logic
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css   # Styling (CSS Grid, Fonts)
│   └── img/            # Generated charts are saved here
├── templates/
│   ├── index.html      # Upload page
│   └── result.html     # Dashboard / Results page
└── uploads/            # Temporary storage for uploaded CSVs

## 🛠️ Tech Stack
Backend: Python (Flask)

Data Processing: Pandas

Visualization: Matplotlib

Frontend: HTML5, CSS3 (Custom styling)

## 📝 Context
This project was developed as part of the VITyarthi "Build Your Own Project" initiative. The goal was to create a functional, user-friendly data analysis tool that solves a real-world student problem (tracking attendance criteria).
