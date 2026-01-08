import pandas as pd

def generate_analytics(sample_data: list) -> pd.DataFrame:
    df = pd.DataFrame(sample_data)

    # Challenge1: Filter to include only respondents who have given a productivity rating
    df = df[
        df["How would you rate your productivity when working remotely?"].notna()
    ]
    

    # Create a morale score based on agreement levels with statements about remote work collaboration and recommendations
    def morale_score(row):
        score = 0
        agree_mapping = {
            'Strongly agree': 3,
            'Somewhat agree': 2,
            'Neither agree nor disagree': 1,
            'Somewhat disagree': 0,
            'Strongly disagree': 0,
            None: 0,
            float('nan'): 0,
        }
        score += agree_mapping.get(row['Thinking about remote working in the last 3 months, how strongly do you agree or disagree with the following statements? - I could easily collaborate with colleagues when working remotely'], 0)
        score += agree_mapping.get(row['Thinking about remote working in the last 3 months, how strongly do you agree or disagree with the following statements? - I would recommend remote working to others'], 0)
        return score

    df['morale_score'] = df.apply(morale_score, axis=1)

    # Challenge2: Select columns relevant to morale and well-being analysis
    df = df[[ 'Which of the following best describes your industry?',
            'Which of the following best describes your household?',
            'How would you rate your productivity when working remotely?',
            'morale_score' ]]

    # Aggregate mean morale scores by industry and household type
    morale_by_group = df.groupby(['Which of the following best describes your industry?', 'Which of the following best describes your household?'])['morale_score'].mean().reset_index()
    moral_sorted = morale_by_group.sort_values(by='morale_score', ascending=False)

    return moral_sorted

