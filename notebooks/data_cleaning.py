import pandas as pd
import numpy as np

# Load raw data
df_2020 = pd.read_csv('../data/raw/2020_rws.csv', encoding='cp1252')
df_2021 = pd.read_csv('../data/raw/2021_rws.csv', encoding='cp1252')

print("Loaded 2020:", df_2020.shape)
print("Loaded 2021:", df_2021.shape)

# ============================================
# STEP 1: Select columns for 2020 by index
# ============================================

# Based on our analysis, these are the columns we need:
columns_2020_indices = [
    0,   # Response ID
    1,   # Birth year
    2,   # Gender
    3,   # Industry
    5,   # Occupation
    7,   # Org size
    8,   # Is manager
    9,   # Household type
    10,  # Tenure
    11,  # Metro/Regional
    12,  # Remote time last year
    19,  # Preferred remote time last year
    20,  # Remote time last 3 months
    21,  # Org encouraged remote (last 3 months)
    22,  # Org prepared
    23,  # Remote was common
    24,  # Easy permission
    25,  # Easy collaboration
    27,  # Preferred remote time last 3 months
    28,  # Post-COVID remote preference
    29,  # Expect employer encourage
    30,  # Expect employer changes
    31,  # Expect more choice
    32,  # PRODUCTIVITY
    33,  # Office day - commute hours
    34,  # Office day - working hours
    35,  # Office day - personal hours
    36,  # Office day - caring hours
    37,  # Remote day - commute hours
    38,  # Remote day - working hours
    39,  # Remote day - personal hours
    40,  # Remote day - caring hours
]

# Select those columns
df_2020_selected = df_2020.iloc[:, columns_2020_indices].copy()

print(f"\n2020 after selection: {df_2020_selected.shape}")
print("\nSelected columns:")
for i, col in enumerate(df_2020_selected.columns):
    print(f"  {i}: {col[:60]}...")
    

# ============================================
# STEP 2: Rename columns to something readable
# ============================================

# Create a mapping of old names to new names
new_column_names = [
    'response_id',
    'birth_year',
    'gender',
    'industry',
    'occupation',
    'org_size',
    'is_manager',
    'household_type',
    'tenure',
    'location',
    'remote_time_last_year',
    'preferred_remote_last_year',
    'remote_time_last_3months',
    'org_encouraged_remote',
    'org_prepared',
    'remote_was_common',
    'easy_permission',
    'easy_collaboration',
    'preferred_remote_last_3months',
    'post_covid_preference',
    'expect_employer_encourage',
    'expect_employer_changes',
    'expect_more_choice',
    'productivity_remote',
    'office_commute_hrs',
    'office_working_hrs',
    'office_personal_hrs',
    'office_caring_hrs',
    'remote_commute_hrs',
    'remote_working_hrs',
    'remote_personal_hrs',
    'remote_caring_hrs'
]

# Apply the new names
df_2020_selected.columns = new_column_names

print("\n" + "="*60)
print("2020 COLUMNS AFTER RENAMING")
print("="*60)
for col in df_2020_selected.columns:
    print(f"  - {col}")

# Add a year column so we know which dataset this is from
df_2020_selected['year'] = 2020

print(f"\nFinal 2020 shape: {df_2020_selected.shape}")

# Preview the cleaned data
print("\n" + "="*60)
print("PREVIEW OF CLEANED 2020 DATA")
print("="*60)
print(df_2020_selected.head())

# ============================================
# STEP 3: Now do the same for 2021
# ============================================

print("\n" + "="*60)
print("2021 COLUMNS WITH INDEX")
print("="*60)
for i, col in enumerate(df_2021.columns):
    print(f"{i}: {col[:80]}")

    # ============================================
# STEP 4: Select and rename 2021 columns
# ============================================

columns_2021_indices = [
    0,   # Response ID
    1,   # Birth year
    2,   # Gender
    4,   # Industry
    5,   # Occupation
    6,   # Org size
    96,  # Is manager (moved in 2021)
    7,   # Household type
    3,   # Tenure
    8,   # Location (Metro/Regional)
    9,   # Remote time Q4 2020
    10,  # Preferred remote Q4 2020
    11,  # Remote time 2021
    25,  # Org encouraged remote
    26,  # Org prepared
    27,  # Remote was common
    28,  # Easy permission
    29,  # Easy collaboration
    12,  # Preferred remote 2021
    13,  # Post-COVID preference
    34,  # Expect employer encourage
    35,  # Expect employer changes
    36,  # Expect more choice
    107, # Productivity
    37,  # Office - commute
    38,  # Office - working
    39,  # Office - personal
    40,  # Office - caring
    42,  # Remote - commute
    43,  # Remote - working
    44,  # Remote - personal
    45,  # Remote - caring
    # 2021-ONLY columns (wellbeing & policy)
    93,  # Feel better remote
    94,  # More active remote
    95,  # Feel better in person
    24,  # Policy sentiment
]

df_2021_selected = df_2021.iloc[:, columns_2021_indices].copy()

print(f"\n2021 after selection: {df_2021_selected.shape}")

# Rename columns
new_column_names_2021 = [
    'response_id',
    'birth_year',
    'gender',
    'industry',
    'occupation',
    'org_size',
    'is_manager',
    'household_type',
    'tenure',
    'location',
    'remote_time_last_year',
    'preferred_remote_last_year',
    'remote_time_this_year',
    'org_encouraged_remote',
    'org_prepared',
    'remote_was_common',
    'easy_permission',
    'easy_collaboration',
    'preferred_remote_this_year',
    'post_covid_preference',
    'expect_employer_encourage',
    'expect_employer_changes',
    'expect_more_choice',
    'productivity_remote',
    'office_commute_hrs',
    'office_working_hrs',
    'office_personal_hrs',
    'office_caring_hrs',
    'remote_commute_hrs',
    'remote_working_hrs',
    'remote_personal_hrs',
    'remote_caring_hrs',
    # 2021-only
    'feel_better_remote',
    'more_active_remote',
    'feel_better_in_person',
    'policy_sentiment'
]

df_2021_selected.columns = new_column_names_2021
df_2021_selected['year'] = 2021

print(f"Final 2021 shape: {df_2021_selected.shape}")
print("\n2021 Columns:")
for col in df_2021_selected.columns:
    print(f"  - {col}")

    # ============================================
# STEP 5: Combine the datasets
# ============================================

# First, let's see what columns are common vs unique
print("\n" + "="*60)
print("COMPARING COLUMNS")
print("="*60)

cols_2020 = set(df_2020_selected.columns)
cols_2021 = set(df_2021_selected.columns)

common_cols = cols_2020.intersection(cols_2021)
only_2020 = cols_2020 - cols_2021
only_2021 = cols_2021 - cols_2020

print(f"\nCommon columns: {len(common_cols)}")
print(f"Only in 2020: {only_2020}")
print(f"Only in 2021: {only_2021}")

# ============================================
# STEP 6: Create combined dataset (common columns only)
# ============================================

common_cols_list = list(common_cols)
df_combined = pd.concat([
    df_2020_selected[common_cols_list],
    df_2021_selected[common_cols_list]
], ignore_index=True)

print(f"\nCombined dataset shape: {df_combined.shape}")

# ============================================
# STEP 7: Quick data quality check
# ============================================

print("\n" + "="*60)
print("DATA QUALITY CHECK")
print("="*60)

print("\nMissing values in combined dataset:")
missing = df_combined.isnull().sum()
missing_pct = (missing / len(df_combined) * 100).round(1)
for col in df_combined.columns:
    if missing[col] > 0:
        print(f"  {col}: {missing[col]} ({missing_pct[col]}%)")

print("\nData types:")
print(df_combined.dtypes)

# ============================================
# STEP 8: Save the cleaned datasets
# ============================================

# Save to the processed folder
df_2020_selected.to_csv('../data/processed/2020_cleaned.csv', index=False)
df_2021_selected.to_csv('../data/processed/2021_cleaned.csv', index=False)
df_combined.to_csv('../data/processed/combined_cleaned.csv', index=False)

print("\n" + "="*60)
print("FILES SAVED!")
print("="*60)
print("  - ../data/processed/2020_cleaned.csv")
print("  - ../data/processed/2021_cleaned.csv")
print("  - ../data/processed/combined_cleaned.csv")

print(f"\nReady for Power BI! 🎉")