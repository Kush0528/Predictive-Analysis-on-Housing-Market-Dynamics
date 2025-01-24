# Predictive-Analysis-on-Housing-Market-Dynamics

## Project Overview
This project aims to develop a machine learning model that predicts how new constructions impact median house sales prices, specifically focusing on regional effects on housing markets. The primary stakeholders are builders and developers who need precise and actionable insights to optimize their construction planning and pricing strategies effectively. 

## Data Sources 
- US Census Bureau (http://www.census.gov/construction/nrc/index.html) 
- Zillow Research (https://www.zillow.com/research/data/).

## Exploratory Data Analysis (EDA)
For exploratory data analysis (EDA), various data visualization tools were employed to plot distributions, detect outliers, and identify patterns. This phase was crucial for feature selection, as it helped to determine which variables had the most significant impact on housing prices. By using correlation matrices and scatter plots, the interactions between variables were accessed and explored how regional differences might influence market dynamics.

## Data Preprocessing
Missing values were addressed by using 'forward and backward filling' techniques, which were especially effective in preserving accurate temporal sequences in the data, essential for time series analysis. To mitigate potential scale bias within the dataset, 'normalization' and 'feature scaling' were applied to all numeric inputs, ensuring that larger-scale variables would not disproportionately affect the model outcomes.

## Model Development
- Initial Model Trials - Started with simpler models, such as 'linear regression', to establish a baseline understanding of the data. 
- Advanced Machine Learning Models - Shifted focus to more advanced models that could handle complex interactions, specifically 'XGBoost', 'Random Forest', and 'Gradient Boosting'. 
- Target Variable Specification - Clearly defined the target variable. 
- Hyperparameter Tuning - To further refine models, extensive hyperparameter tuning was conducted using grid search techniques. 
- Cross-Validation - To prevent overfitting and assess the generalizability of models, cross-validation technique was utilized. 

## Results
'XGBoost' achieved impressive results, recording a Mean Absolute Error (MAE) of $35,781.40, which reflects a high level of predictive accuracy in monetary terms. Additionally, the model reached an R² (Coefficient of Determination) of 0.8612, indicating a strong fit and the ability to explain a significant portion of the variance in housing prices.

## Feature Importance Analysis
Analysis using SHAP values showed that factors like new construction counts and market heat indexes play crucial roles in influencing housing prices. The SHAP summary plot visually highlights the impact of these features. Higher values of these factors significantly drive the model's predictions, reflecting the real-world dynamics observed in housing markets.

## Prototype Development
![Image](https://github.com/user-attachments/assets/232bd828-4ead-4757-b667-5279153964c5)
To translate model's capabilities into a practical application, 'Real Estate Price Prediction Dashboard' was developed. This interactive dashboard allows users to select a prediction model, choose a city, and specify additional housing units to see their impact on prices in real-time.

## Conclusion
This project marks a significant advancement in using machine learning to understand and predict how new constructions impact housing prices. The models created through this initiative offer stakeholders valuable tools for forecasting and planning for market changes.
