# Attendance Analyzer (Flask) — Aesthetic UI

## Overview
A lightweight Flask web app that analyzes attendance data from a CSV and displays subject-wise percentages and modern visualizations. This version has a minimal, Apple-like aesthetic with an accent color of #007AFF and a card-grid layout for subjects.

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

## Notes
- The original VITyarthi project guidelines PDF you uploaded is referenced here: `/mnt/data/BuildYourOwnProject.pdf`