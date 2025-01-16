# Medical-Data-Visualizer
Description
The Medical Data Visualizer project is a Python-based data analysis tool designed to process and visualize medical examination data. The objective of this analysis is to explore trends, highlight patterns, and derive meaningful insights about the health status of individuals based on categorical and numerical medical data.

Key Features
Data Cleaning and Normalization:
  Added a calculated overweight feature based on BMI values.
  Normalized cholesterol and gluc values to standardize interpretation.
Categorical Data Visualization:
  Used a categorical plot to display the distribution of health-related features (cholesterol, gluc, smoke, alco, active, overweight) split by cardiovascular condition (cardio).
Correlation Heatmap:
  Generated a heatmap to highlight the relationships between various numerical medical metrics (e.g., blood pressure, BMI, age).
  Applied filtering to remove outliers and ensure meaningful correlations.
Tools and Libraries
  Python: For data manipulation and analysis.
  Pandas: Used for data processing and cleaning.
  Seaborn: For creating advanced visualizations like categorical plots and heatmaps.
  Matplotlib: To support plotting and graphical outputs.
