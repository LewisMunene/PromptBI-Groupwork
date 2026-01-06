# 🤝 Contributing Guidelines

Welcome to the Remote Work Analysis project! This document outlines how we work together as a team.

## 📋 Before You Start

1. **Join our WhatsApp group** for real-time communication
2. **Clone the repository** to your local machine or open in Google Colab
3. **Check the project board** (Issues tab) for available tasks

## 🔀 Git Workflow

We use a **feature branch workflow** to keep our main branch clean.

### Step 1: Get the Latest Code
```bash
git checkout main
git pull origin main
```

### Step 2: Create Your Branch
```bash
git checkout -b feature/[your-name]-[task-description]

# Examples:
git checkout -b feature/lewis-productivity-analysis
git checkout -b feature/jane-powerbi-dashboard
git checkout -b feature/alex-morale-charts
```

### Step 3: Do Your Work
- Make your changes
- Test your code
- Commit frequently with clear messages

### Step 4: Commit Your Changes
```bash
git add .
git commit -m "Add: [brief description of what you did]"

# Good commit messages:
# "Add: productivity analysis notebook with statistical tests"
# "Update: cleaned dataset with missing values handled"
# "Fix: chart labels on morale visualization"
```

### Step 5: Push & Create Pull Request
```bash
git push origin feature/your-branch-name
```
Then go to GitHub and create a Pull Request!

## 📁 File Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| Notebooks | `##_description.ipynb` | `02_productivity_analysis.ipynb` |
| Charts | `description_chart.png` | `productivity_by_industry_chart.png` |
| Data files | `lowercase_with_underscores.csv` | `merged_rws_clean.csv` |

## 📊 Notebook Standards

Every analysis notebook should include:

```python
# Header Cell
"""
Title: [Analysis Name]
Author: [Your Name]
Date: [Date]
Description: [What this notebook does]
"""

# Imports Cell
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading Cell
df = pd.read_csv('../data/processed/merged_rws_clean.csv')
```

## 🎨 Visualization Standards

To keep our dashboard consistent:

- **Color Palette:** Use consistent colors across all charts
- **Font:** Keep labels readable
- **Titles:** Every chart needs a clear title
- **Source:** Note data source if relevant

## ✅ Code Review Checklist

Before merging, ensure:
- [ ] Code runs without errors
- [ ] Findings are documented in markdown cells
- [ ] Charts have clear titles and labels
- [ ] No sensitive data committed
- [ ] Branch is up to date with main

## 🆘 Need Help?

- **Git issues?** Tag Lewis in WhatsApp
- **Analysis questions?** Post in the group
- **PowerBI help?** Ask [PowerBI team member]

## 📞 Communication

- **Quick questions:** WhatsApp group
- **Code discussions:** GitHub Pull Request comments
- **Meetings:** Monday, January 5th and as scheduled

---

Remember: There are no stupid questions! We're all learning together. 💪