import csv
from statistics import mean, median
from fpdf import FPDF

# Step 1: Read data from CSV
def read_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['Name'], int(row['Score'])) for row in reader]
    return data

# Step 2: Analyze data
def analyze_data(data):
    scores = [score for _, score in data]
    return {
        'Total Students': len(scores),
        'Average Score': mean(scores),
        'Median Score': median(scores),
        'Highest Score': max(scores),
        'Lowest Score': min(scores),
    }

# Step 3: Generate PDF report
def generate_pdf(data, analysis, filename='report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Student Score Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, "Individual Scores:", ln=True)

    for name, score in data:
        pdf.cell(200, 10, f"{name}: {score}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, "Summary Statistics:", ln=True)

    pdf.set_font("Arial", size=12)
    for key, value in analysis.items():
        pdf.cell(200, 10, f"{key}: {value}", ln=True)

    pdf.output(filename)
    print(f"PDF report saved as: {filename}")

# Main
if __name__ == "__main__":
    data = read_data('data.csv')
    analysis = analyze_data(data)
    generate_pdf(data, analysis)
