# Project Report - Attendance Analyzer (Flask)

## 1. Cover Page
Attendance Analyzer - Flask Web App

## 2. Introduction
This project is a simple web application that helps students analyze attendance data from CSV files. It calculates subject-wise attendance percentages and visualizes them.

## 3. Problem Statement
Calculating attendance manually can be error-prone and time-consuming. This app automates that.

## 4. Functional Requirements
- Upload CSV
- Process supported CSV formats
- Display subject-wise report
- Generate charts

## 5. Non-Functional Requirements
- Usability: simple web UI
- Performance: handles small CSVs (< 10k rows) quickly
- Reliability: input validation
- Maintainability: modular Python code

## 6. System Architecture
Single-server Flask app. Components: Web frontend, Analyzer (pandas), Visualizer (matplotlib), Storage (uploads folder).

## 7. Design Diagrams
See UML folder files.

## 8. Design Decisions & Rationale
- Chose Flask for quick web UI
- Pandas for CSV processing
- Matplotlib for charts (no external JS libraries)

## 9. Implementation Details
Code files: app.py, templates, static, uploads.

## 10. Screenshots / Results
Use the sample CSV to generate charts.

## 11. Testing Approach
- Manual testing with sample CSVs
- Edge-case: missing columns are reported as error

## 12. Challenges Faced
- Supporting multiple CSV formats gracefully

## 13. Learnings & Key Takeaways
- Quick prototyping with Flask + Pandas

## 14. Future Enhancements
- Add authentication
- Per-student reports and export to PDF
- Threshold configuration
- Downloadable Excel/PDF reports

## 15. References
VITyarthi BuildYourOwnProject.pdf at `/mnt/data/BuildYourOwnProject.pdf`