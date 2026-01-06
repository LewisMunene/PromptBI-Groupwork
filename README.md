# 📊 Remote Work Impact Analysis: Post-Pandemic Policy Recommendations

[![Contributors](https://img.shields.io/badge/Contributors-4-brightgreen)]()
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()
[![Dataset](https://img.shields.io/badge/Dataset-RWS%202020%20%26%202021-blue)]()

## 🎯 Project Overview

**Objective:** Analyze Remote Working Survey (RWS) data from 2020-2021 to assess how remote work affects productivity and employee morale, then propose an ideal post-pandemic work policy based on our findings.

**Course:** PromptBI Data Analytics Program  
**Submission:** Single, well-structured dashboard with key insights, visualizations, and recommendations

---

## 👥 Team Members & Responsibilities

| Member | Role | Primary Tasks | Tools |
|--------|------|---------------|-------|
| Lewis Munene | Project Lead / Data Analyst | Data cleaning, EDA, Productivity analysis | Python, Pandas, Claude AI |
| [Member 2] | Visualization Specialist | Dashboard development | PowerBI |
| [Member 3] | Statistical Analyst | Morale & wellbeing analysis | Python/Excel |
| [Member 4] | Research & Documentation | Narrative synthesis, recommendations | - |

---

## 📁 Project Structure

```
PromptBI-Groupwork/
│
├── README.md                    # Project overview & findings summary
├── CONTRIBUTING.md              # How to contribute guidelines
│
├── data/
│   ├── raw/                     # Original datasets (DO NOT MODIFY)
│   │   ├── 2020_rws.csv
│   │   ├── 2021_rws.csv
│   │   └── data_dictionary.md
│   └── processed/               # Cleaned/transformed datasets
│       └── merged_rws_clean.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb           # Data prep & quality checks
│   ├── 02_productivity_analysis.ipynb   # Productivity deep-dive
│   ├── 03_morale_wellbeing.ipynb        # Employee morale analysis
│   ├── 04_yoy_comparison.ipynb          # 2020 vs 2021 trends
│   └── 05_policy_recommendations.ipynb  # Final synthesis
│
├── visualizations/
│   ├── charts/                  # Individual chart exports
│   └── dashboard/               # PowerBI files & exports
│       └── remote_work_dashboard.pbix
│
├── reports/
│   ├── executive_summary.md     # TL;DR for stakeholders
│   └── full_analysis.md         # Detailed narrative
│
└── docs/
    ├── meeting_notes/           # Team meeting records
    └── references/              # Research & citations
```

---

## 📈 Key Research Questions

### 1. Productivity Impact
- How does self-reported productivity differ between remote and in-office work?
- Which demographics report the highest/lowest remote productivity?
- Do managers perceive remote productivity differently than individual contributors?

### 2. Employee Morale & Wellbeing
- What are the biggest barriers to remote work satisfaction?
- How has morale changed from 2020 (forced remote) to 2021 (hybrid emergence)?
- What factors predict employee preference for remote work?

### 3. Policy Implications
- What is the optimal remote work percentage preferred by employees?
- How willing are employees to trade compensation for flexibility?
- What policies should organizations implement post-pandemic?

---

## 🔍 Key Findings

> **Note:** This section will be updated as analysis progresses

### Finding 1: [Title]
*Owner: [Member Name]*

[Brief description of finding with supporting visualization]

![Visualization placeholder](visualizations/charts/finding1.png)

---

### Finding 2: [Title]
*Owner: [Member Name]*

[Brief description of finding with supporting visualization]

---

### Finding 3: [Title]
*Owner: [Member Name]*

[Brief description of finding with supporting visualization]

---

## 📊 Final Dashboard

> **[Link to Interactive Dashboard]** *(PowerBI/Tableau Public link)*

![Dashboard Preview](visualizations/dashboard/dashboard_preview.png)

### Dashboard Components:
1. **Overview Tab** - Key metrics at a glance
2. **Productivity Analysis** - Remote vs in-office productivity breakdown
3. **Employee Morale** - Satisfaction drivers and barriers
4. **Policy Recommendations** - Data-driven suggestions

---

## 🎯 Recommendations

Based on our analysis, we recommend the following post-pandemic work policy:

1. **[Recommendation 1]**
   - Supporting evidence: [metric/finding]
   
2. **[Recommendation 2]**
   - Supporting evidence: [metric/finding]

3. **[Recommendation 3]**
   - Supporting evidence: [metric/finding]

---

## 🛠️ Tools & Technologies

| Purpose | Tool |
|---------|------|
| Data Processing | Python (Pandas, NumPy) |
| Statistical Analysis | Python (SciPy, Statsmodels) |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | PowerBI |
| Collaboration | GitHub, Google Colab |
| AI Assistance | PromptBI, Claude AI |

---

## 📅 Project Timeline

| Phase | Tasks | Deadline | Status |
|-------|-------|----------|--------|
| Week 1 | Data exploration & cleaning | [Date] | 🔄 In Progress |
| Week 1 | Individual analysis assignments | [Date] | ⏳ Pending |
| Week 2 | Visualization development | [Date] | ⏳ Pending |
| Week 2 | Dashboard creation | [Date] | ⏳ Pending |
| Week 3 | Integration & narrative | [Date] | ⏳ Pending |
| Week 3 | Final review & submission | [Date] | ⏳ Pending |

---

## 🚀 Getting Started

### Prerequisites
```bash
# Clone the repository
git clone https://github.com/LewisMunene/PromptBI-Groupwork.git

# Install dependencies (if using Python locally)
pip install pandas numpy matplotlib seaborn scipy
```

### For Google Colab Users
1. Open [Google Colab](https://colab.research.google.com/)
2. File → Open Notebook → GitHub tab
3. Enter: `https://github.com/LewisMunene/PromptBI-Groupwork`
4. Select the notebook you want to work on

### Data Access
The raw datasets are available in the `data/raw/` folder. Always work from the processed data in `data/processed/` for consistency.

---

## 📝 Contribution Guidelines

1. **Never commit directly to `main`** - Create a feature branch
2. **Naming convention:** `feature/[your-name]-[task]` (e.g., `feature/lewis-productivity-analysis`)
3. **Commit messages:** Use clear, descriptive messages
4. **Pull Requests:** Required for merging - tag at least one teammate for review

### Workflow:
```bash
# Create your branch
git checkout -b feature/your-name-task

# Make changes, then commit
git add .
git commit -m "Add: productivity analysis for managers"

# Push to GitHub
git push origin feature/your-name-task

# Create Pull Request on GitHub
```

---

## 📧 Contact

For questions about this project, reach out to:
- **Lewis Munene** (Project Lead) - [GitHub](https://github.com/LewisMunene)
- **PromptBI Collab Group** - WhatsApp Group

---

## 📜 License

This project is for educational purposes as part of the PromptBI Data Analytics Program.

---

*Last Updated: January 2026*