from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
STATIC_IMG = os.path.join(os.path.dirname(__file__), 'static', 'img')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_IMG, exist_ok=True)

def analyze_attendance(csv_path):
    df = pd.read_csv(csv_path)
    # Expecting columns: Student, Subject, Attended, Total (Attended and Total per subject or boolean per class)
    # Support two formats:
    # 1) Rows per subject with 'Attended' and 'Total' numeric columns
    # 2) Rows per class with 'Present' column (1/0) and 'Subject'
    result = {}
    if {'Attended','Total'}.issubset(df.columns):
        # Aggregate by subject
        agg = df.groupby('Subject').sum()[['Attended','Total']]
        agg['Percentage'] = (agg['Attended'] / agg['Total']) * 100
        for subj, row in agg.iterrows():
            result[subj] = {
                'attended': int(row['Attended']),
                'total': int(row['Total']),
                'percentage': round(row['Percentage'],2)
            }
    elif 'Present' in df.columns and 'Subject' in df.columns:
        agg = df.groupby('Subject').agg({'Present':'sum','Subject':'count'})
        agg = agg.rename(columns={'Present':'Attended','Subject':'Total'})
        agg['Percentage'] = (agg['Attended'] / agg['Total']) * 100
        for subj, row in agg.iterrows():
            result[subj] = {
                'attended': int(row['Attended']),
                'total': int(row['Total']),
                'percentage': round(row['Percentage'],2)
            }
    else:
        # Try per-student summary if Student and Present exist
        if 'Student' in df.columns and 'Present' in df.columns:
            agg = df.groupby('Student').agg({'Present':'sum','Present':'count'})
            for student, row in agg.iterrows():
                attended = int(row['Present'])
                total = int(row['Present'])
                result[student] = {
                    'attended': attended,
                    'total': total,
                    'percentage': round((attended/total)*100,2) if total>0 else 0
                }
        else:
            raise ValueError("CSV format not recognized. Required columns: ['Subject','Attended','Total'] or ['Subject','Present']")

    # Overall stats
    overall_attended = sum([v['attended'] for v in result.values()])
    overall_total = sum([v['total'] for v in result.values()]) or 1
    overall_pct = round((overall_attended/overall_total)*100,2)
    overall = {'attended': overall_attended, 'total': overall_total, 'percentage': overall_pct}
    return result, overall

def make_bar_chart(result, out_path):
    subjects = list(result.keys())
    percentages = [result[s]['percentage'] for s in subjects]
    plt.figure(figsize=(8,4))
    plt.bar(subjects, percentages)
    plt.ylim(0,100)
    plt.ylabel("Attendance %")
    plt.xlabel("Subject")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def make_pie_chart(result, out_path):
    subjects = list(result.keys())
    percentages = [result[s]['percentage'] for s in subjects]
    if len(percentages)==0:
        return
    plt.figure(figsize=(6,6))
    plt.pie(percentages, labels=subjects, autopct='%1.1f%%')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        f = request.files.get('file')
        if not f:
            return render_template('index.html', error="No file uploaded")
        save_path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(save_path)
        try:
            result, overall = analyze_attendance(save_path)
        except Exception as e:
            return render_template('index.html', error=str(e))
        # Generate charts
        bar_path = os.path.join('static','img','bar.png')
        pie_path = os.path.join('static','img','pie.png')
        make_bar_chart(result, os.path.join(os.path.dirname(__file__), bar_path))
        make_pie_chart(result, os.path.join(os.path.dirname(__file__), pie_path))
        return render_template('result.html', result=result, overall=overall, bar_img='/' + bar_path, pie_img='/' + pie_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)