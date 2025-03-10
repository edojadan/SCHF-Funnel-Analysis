# SCHF Competitor Funnel Analysis

This project analyzes the donor funnel of Sydney Children's Hospitals Foundation (SCHF) to provide insights into nonprofit customer retention and fundraising performance.

## Project Structure

```
SCHF-Competitor-Funnel-Analysis/
│── data/
│   ├── schf_funnel_data.csv  # Data file containing the funnel stages
│── analysis/
│   ├── funnel_analysis.py    # Script to process and analyze the data
│   ├── visualizations.py     # Generates graphs and insights
│── reports/
│   ├── schf_funnel_analysis_report.md  # Summary of findings
│── README.md
```

## How to Open and Run the Project

### 1. Install Python (if not already installed)
This project requires Python **3.7 or later**.  
If you don’t have Python installed, you can download it here:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Clone or Download the Project
To get started, **clone the repository** using Git:
```sh
git clone https://github.com/edojadan/SCHF-Competitor-Funnel-Analysis.git
cd SCHF-Competitor-Funnel-Analysis
```
Alternatively, you can **download the ZIP file**, extract it, and navigate into the project folder.

### 3. Create a Virtual Environment (Optional but Recommended)
Setting up a virtual environment ensures that dependencies don’t interfere with other projects.
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 4. Install Required Dependencies
Install the necessary Python libraries using:
```sh
pip install pandas matplotlib
```

### 5. Run the Analysis
To process and analyze the funnel data, run:
```sh
python analysis/funnel_analysis.py
```
This will display the **stages, user drop-offs, and retention rates**.

### 6. Generate Visualizations
To view funnel performance graphs, run:
```sh
python analysis/visualizations.py
```
This will generate:
- **Funnel User Progression (Bar Chart)**
- **Drop-off Rate Analysis (Line Graph)**

### 7. Read the Report
After running the analysis, check the findings in:
```
reports/schf_funnel_analysis_report.md
```
It summarizes:
- Donor engagement trends
- Funnel stage weaknesses
- Recommendations for improving nonprofit conversions

## Key Features
- **Real-world Nonprofit Data** – Uses publicly available SCHF fundraising insights.  
- **Automated Analysis** – Computes drop-off rates and conversion trends.  
- **Data Visualizations** – Generates graphs for easy understanding.  
- **Strategic Insights** – Helps nonprofits optimize their marketing funnel.

## What I Enjoyed
I really enjoyed working with real-world nonprofit data and drawing meaningful insights from it. Seeing how donor retention can be improved through strategic engagement was fascinating. Analyzing drop-off points and optimizing the funnel felt like solving a puzzle, and it was satisfying to uncover key areas where improvements could make a big impact.

## Next Steps
- Compare insights with other nonprofit case studies.  
- Adjust strategies to **increase supporter engagement & retention**.  
- Expand analysis to include **multi-channel marketing data (social media, email, events, etc.)**.

## Sources

- https://www.theaustralian.com.au/business/growth-agenda/childrens-charity-borrows-from-retail-sector-for-story-of-growth/news-story/4bfead86c5cab9607e342836bef66e00

- https://www.wildapricot.com/blog/nonprofit-marketing-funnels

- https://en.wikipedia.org/wiki/Cause-related_loyalty_marketing