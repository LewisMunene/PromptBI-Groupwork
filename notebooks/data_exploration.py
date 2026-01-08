import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df_2020 = pd.read_csv('../data/raw/2020_rws.csv', encoding='cp1252')
df_2021 = pd.read_csv('../data/raw/2021_rws.csv', encoding='cp1252')

# Display basic information about the datasets
print("2020 Dataset Info:", df_2020.shape)
print("2021 Dataset Info:", df_2021.shape)

# ============================================
# STEP 1: View columns more readably (first 50 chars)
# ============================================
print("\n" + "="*60)
print("2020 COLUMNS (truncated)")
print("="*60)
for i, col in enumerate(df_2020.columns):
    print(f"{i}: {col[:50]}...")

print("\n" + "="*60)
print("2021 COLUMNS (truncated)")
print("="*60)
for i, col in enumerate(df_2021.columns):
    print(f"{i}: {col[:50]}...")

# ============================================
# STEP 2: Check data types
# ============================================
print("\n" + "="*60)
print("2020 DATA TYPES")
print("="*60)
print(df_2020.dtypes)

# ============================================
# STEP 3: Check for missing values
# ============================================
print("\n" + "="*60)
print("2020 MISSING VALUES (top 10)")
print("="*60)
missing_2020 = df_2020.isnull().sum().sort_values(ascending=False)
print(missing_2020.head(10))

print("\n" + "="*60)
print("2021 MISSING VALUES (top 10)")
print("="*60)
missing_2021 = df_2021.isnull().sum().sort_values(ascending=False)
print(missing_2021.head(10))

# ============================================
# STEP 4: Preview actual data (first 3 rows)
# ============================================
print("\n" + "="*60)
print("2020 FIRST 3 ROWS")
print("="*60)
print(df_2020.head(3))



# ============================================
# STEP 5: Find columns relevant to our analysis
# ============================================

# Let's search for keywords in column names
def find_columns(df, keyword):
    """Find columns containing a keyword"""
    matches = [col for col in df.columns if keyword.lower() in col.lower()]
    return matches

print("\n" + "="*60)
print("FINDING RELEVANT COLUMNS FOR OUR ANALYSIS")
print("="*60)

# Productivity
print("\n📊 PRODUCTIVITY columns (2020):")
for col in find_columns(df_2020, 'productive'):
    print(f"  - {col[:70]}...")

print("\n📊 PRODUCTIVITY columns (2021):")
for col in find_columns(df_2021, 'productive'):
    print(f"  - {col[:70]}...")

# Wellbeing/Morale
print("\n😊 WELLBEING columns (2021):")
for col in find_columns(df_2021, 'feel better'):
    print(f"  - {col[:70]}...")
for col in find_columns(df_2021, 'active'):
    print(f"  - {col[:70]}...")

# Remote work preferences
print("\n🏠 REMOTE PREFERENCE columns (2020):")
for col in find_columns(df_2020, 'prefer'):
    print(f"  - {col[:70]}...")

# Policy
print("\n📋 POLICY columns (2021):")
for col in find_columns(df_2021, 'policy'):
    print(f"  - {col[:70]}...")

# Time allocation
print("\n⏰ TIME ALLOCATION columns (2020):")
for col in find_columns(df_2020, 'hours'):
    print(f"  - {col[:70]}...")

# Demographics (these are usually at the start)
print("\n👤 DEMOGRAPHIC columns (first 12 of 2020):")
for col in df_2020.columns[:12]:
    print(f"  - {col[:70]}...")