import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the data
df = pd.read_csv('medical_examination.csv')

# Step 2: Add 'overweight' column
is_overweight = lambda weight, height: 1 if round(weight / ((height / 100) ** 2), 1) > 25 else 0
df['overweight'] = df.apply(lambda row: is_overweight(row['weight'], row['height']), axis=1)

# Step 3: Normalize 'cholesterol' and 'gluc' values
is_good = lambda value: 0 if value <=1 else 1
df['cholesterol'] = df['cholesterol'].apply(is_good)
df['gluc'] = df['gluc'].apply(is_good)

# Step 4: Function to create categorical plot
def draw_cat_plot():
    # Transform data into long format
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat the data to split it by 'cardio'
    df_cat_grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # Create the categorical plot
    cat_plot = sns.catplot(
        x='variable', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='count', 
        height=5, 
        aspect=1
    )
    fig = cat_plot.fig
    

    fig = sns.catplot(
    data=df_cat_grouped,
    x='variable',      
    y='total',         
    hue='value',       
    col='cardio',     
    kind='bar',        
    height=5,       
    aspect=1 )

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(df_heat.corr(), dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(16, 9))

    # 15
    sns.heatmap(df_heat.corr(), mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")


    # 16
    fig.savefig('heatmap.png')
    return fig
draw_cat_plot()
draw_heat_map()