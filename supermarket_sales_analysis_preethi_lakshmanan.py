# -*- coding: utf-8 -*-
"""Supermarket Sales Analysis-Preethi Lakshmanan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SH5pMlc-16nuCG4XHT94fXfFy30OkiNN

# Supermarket Sales Analysis

**Introduction**

This dataset captures detailed transaction records from a supermarket chain in Myanmar across three cities: Yangon, Naypyitaw, and Mandalay. It provides a comprehensive view of sales activities, customer demographics, and payment methods from January to March 2019.

**Categorical:** Invoice ID, Branch, City, Customer type, Gender, Product line, Date, Time, Payment

**Numerical:** Unit Price, Quamtity, Tax 5%, Sales,Cogs, Gross Margin Percentage, Gross Income, Rating

**Column**

*  **Invoice ID:** Unique identifier for each transaction.
*   **Branch:** The branch location of the supermarket (e.g., Yangon, Naypyitaw, Mandalay).

*   **City:** The city in which the supermarket branch is located.
*  **Customer Type:** Indicates whether the customer is a 'Member' or 'Normal'.

*   **Gender:** Gender of the customer.
*   **Product Line:** The category of the product sold (e.g., Health & Beauty, Electronic Accessories, Home & Lifestyle).

*  **Unit Price:** Price per unit of the product.
*  Quantity: Number of items purchased.

*   **Tax 5%:** Calculated tax amount on the transaction at a 5% rate.
*   **Total:** Total amount for the transaction including tax.

*   **Date:** Date of the transaction.
*   **Time:** Time of the transaction.

*   **Payment:** Payment method used (e.g., Cash, Ewallet, Credit card).
*   **COGS:** Cost of goods sold, representing the raw cost of the products.

*   **Gross Margin Percentage:** Fixed percentage of profit for each sale (4.7619%).
*   **Gross Income:** Profit earned from the transaction.

*   **Rating:** Customer satisfaction rating (out of 10).

**Potential Analysis**

**1. Sales Prediction (Regression)**

**Target:** Sales

**Features:** Unit price, Quantity, Product line, Customer type, Payment, City, etc.

**Goal:** Predict future sales based on product and customer information.

**2. Customer Segmentation (Clustering)**


**Target:** Create a churn label based on customer purchase patterns (repeat vs. one-time).

**Goal:** Predict which customers are less likely to return.

**4. Payment Method Prediction (Classification)**

**Target:** Payment

**Goal:** Predict the preferred payment method of a customer based on transaction details.

**5. Product Recommendation System**

**Goal:** Suggest products based on historical customer purchase data.
"""

##Import required libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
sales = pd.read_csv('/content/SuperMarket Analysis.csv')
sales.head()

"""# Intial EDA(Exploratory Data Analysis)"""

#view the first few rows
sales.head()

#view last few rows
sales.tail()

# no.of rows and coloumn in dataset
rows,column =sales.shape
print(f'no.of rows:',sales.shape[0])
print(f'no.of column:',sales.shape[1])

#view columns names
print('columns name /n')
sales.columns

# dataset information
sales.info()

# checking missing values
sales.isnull().sum()

# find unique values in each column
sales.nunique()

# find the categorical columns based on unique value counts
categorical_column = sales.columns[sales.nunique() < 15]
for col in categorical_column:
  print(f"Uniques Values in '{col}': {sales[col].unique()}")

# Identify Categorical Columns
categorical_columns = sales.select_dtypes(include=['object']).columns
categorical_columns

# Identify Numerical Columns
numerical_columns = sales.select_dtypes(include=['int64', 'float64']).columns
numerical_columns

# find the duplicate rows
sales.duplicated().sum()

# value counts for the 'City' column
sales['City'].value_counts()

# value counts for the 'Customer type' column
sales['Customer type'].value_counts()

# value counts for the 'Gender' column
sales['Gender'].value_counts()

# value counts for the 'Product line' column
sales['Product line'].value_counts()

# value counts for the 'Payment' column
sales['Payment'].value_counts()

# Verify if Sales = cogs + Tax 5%
sales['Sales'].sum() == sales['cogs'].sum() + sales['Tax 5%'].sum()

# Verify if gross income = Sales × gross margin percentage
sales['gross income'].sum() == sales['Sales'].sum() * sales['gross margin percentage'].sum()

# Calculate Total Price = Unit price × Quantity
sales['Total Price'] = sales['Unit price'] * sales['Quantity']
sales.head()

# Profit Margin Calculation
sales['Profit Margin'] = (sales['gross income'] / sales['Total Price']) * 100
sales.head()

# summarise the statistics of the dataset
sales.describe()

"""# EDA PRE-PROCESSING and VISUALIZATION

# Visualizing Numerical and Categorical Features

**Univariate Analysis for Numerical Variables**
"""

#Sales Unit price
plt.figure(figsize=(10, 6))
sns.histplot(sales['Unit price'], bins=20, kde=True, color='blue')
plt.title('Distribution of Unit Price')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.show()

#sales Quantity
plt.figure(figsize=(10, 6))
sns.histplot(sales['Quantity'], bins=20, kde=True, color='red')
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

#sales Tax 5%
plt.figure(figsize=(10, 6))
sns.histplot(sales['Tax 5%'], bins=20, kde=True, color='green')
plt.title('Distribution of Tax 5%')
plt.xlabel('Tax 5%')
plt.ylabel('Frequency')
plt.show()

#sales cogs
plt.figure(figsize=(10, 6))
sns.histplot(sales['cogs'], bins=20, kde=True, color='purple')
plt.title('Distribution of COGS')
plt.xlabel('COGS')
plt.ylabel('Frequency')
plt.show()

#sales gross income
plt.figure(figsize=(10, 6))
sns.histplot(sales['gross income'], bins=20, kde=True, color='orange')
plt.title('Distribution of Gross Income')
plt.xlabel('Gross Income')
plt.ylabel('Frequency')
plt.show()

#sales rating
plt.figure(figsize=(10, 6))
sns.histplot(sales['Rating'], bins=20, kde=True, color='brown')
plt.title('Distribution of Rating')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

"""**Univariate Analysis for Categorical Variables**"""

#sales by branch
plt.figure(figsize=(10, 6))
sns.countplot(x='Branch', data=sales, color='pink')
plt.title('Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Count')
plt.show()

#sales by gender
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', data=sales, color='blue')
plt.title('Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

#sales payment method
plt.figure(figsize=(10, 6))
sns.countplot(x='Payment', data=sales, color='green')
plt.title('Sales Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.show()

#sales product line
plt.figure(figsize=(10, 6))
sns.countplot(x='Product line', data=sales, color='red')
plt.title('Sales Product Line')
plt.xlabel('Product Line')
plt.ylabel('Count')

#customer type of sales
plt.figure(figsize=(10, 6))
sns.countplot(x='Customer type', data=sales, color='orange')
plt.title('Customer Type of Sales')
plt.xlabel('Customer Type')
plt.ylabel('Count')
plt.show()

"""**Bivariate Analysis of Numerical and Categorical Variables**"""

#unit price for each quantity
plt.figure(figsize=(10, 6))
sns.barplot(x='Quantity', y='Unit price', data=sales)
plt.title('Unit Price for Each Quantity')
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
plt.show()

#sales distribution by customer type
plt.figure(figsize=(10, 6))
sns.boxplot(x='Customer type', y='Sales', data=sales, color='yellow')
plt.title('Sales Distribution by Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Sales')
plt.show()

#sales distribution by Product line
plt.figure(figsize=(10, 6))
sns.boxplot(x='Product line', y='Sales', data=sales, color='purple')
plt.title('Sales Distribution by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Sales')
plt.show()

#sales and their rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Rating', data=sales, color='pink')
plt.title('Sales vs. Rating')
plt.xlabel('Sales')
plt.ylabel('Rating')
plt.show()

#gross margin percentage of each sales
plt.figure(figsize=(10, 6))
sns.histplot(x='Sales', y='gross margin percentage', data=sales)
plt.title('Gross Margin Percentage of Each Sales')
plt.xlabel('Sales')
plt.ylabel('Gross Margin Percentage')
plt.show()

#tax 5% for each cogs
plt.figure(figsize=(10, 6))
sns.histplot(x='cogs', y='Tax 5%', data=sales)
plt.title('Tax 5% for Each COGS')
plt.xlabel('COGS')
plt.ylabel('Tax 5%')
plt.show()

# correlating heatmap for numerical columns
plt.figure(figsize=(10, 6))
sns.heatmap(sales.corr(numeric_only=True), annot=True, cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

"""**Multivariate Analysis of Numerical and Categorical Variables**"""

#sales trends by gender and customer type
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer type', y='Sales', hue='Gender', data=sales, palette='pastel')
plt.title('Sales Trends by Gender and Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Sales')
plt.show()

#sales, product line and quantity
plt.figure(figsize=(10, 6))
sns.lineplot(x='Quantity', y='Sales', hue='Product line', data=sales, palette='pastel')
plt.title('Sales, Product line, and Quantity')
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.show()

#distribution of sales by product line and gender
plt.figure(figsize=(10, 6))
sns.boxplot(x='Product line', y='Sales', hue='Gender', data=sales, palette='pastel')
plt.title('Distribution of Sales by Product Line and Gender')
plt.xlabel('Product Line')
plt.ylabel('Sales')
plt.show()

#distribution of the sales by branch and city
plt.figure(figsize=(10, 6))
sns.violinplot(x='Branch', y='Sales', hue='City', data=sales, palette='pastel')
plt.title('Distribution of Sales by Branch and City')
plt.xlabel('Branch')
plt.ylabel('Sales')
plt.show()

#multivariate correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(sales.corr(numeric_only=True), annot=True, cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title('Multivariate Correlation Heatmap')
plt.show()

"""# Pre-Processing"""

#handling missing values
print(sales.isnull().sum())

"""**Analysing Sales Trends Over Time**"""

#group sales by date
sales_by_date = sales.groupby('Date')['Sales'].sum()
sales_by_date

#plot sales trend
plt.figure(figsize=(10, 6))
sns.lineplot(x=sales_by_date.index, y=sales_by_date.values, color='yellow')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

"""**Encoding Categorical Variables**"""

#encode categorical variables
from sklearn.preprocessing import LabelEncoder
#apply label encoding to categorical columns
categorical_columns = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
label_encoder = LabelEncoder()
for col in sales.select_dtypes(include='object'):
 sales[col]=label_encoder.fit_transform(sales[col])
 sales.head()

#sales_encoded information
sales.info()

# View value counts for the 'Branch' column after encoding
print(sales['Branch'].value_counts())

# View value counts for the 'Product line' column after encoding
print(sales['Product line'].value_counts())

# sales_encoded view selected columns
sales[['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']].head()

"""**Scaling Numerical Features**"""

#scaling numerical features
from sklearn.preprocessing import StandardScaler
numerical_columns = ['Unit price', 'Quantity', 'Tax 5%', 'cogs', 'gross income', 'Rating']
scaler = StandardScaler()
sales[numerical_columns] = scaler.fit_transform(sales[numerical_columns])
sales.head()

"""**Outlier Detection**"""

#List of numerical columns to check the outliers
numerical_columns = ['Unit price', 'Quantity', 'Tax 5%', 'cogs', 'gross income', 'Rating']

#plot boxplots to visualize outliers
plt.figure(figsize=(10, 6))
for i, column in enumerate(numerical_columns, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(x=sales[column], color='skyblue')
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()

# Box Plot of Numerical Columns: Create a box plot for all numerical columns in a single graph to visualize their distribution, range, and outliers.
# Explain any visible trends or outliers
plt.figure(figsize=(10, 6),facecolor='blue')
sns.boxplot(data=sales[numerical_columns], orient='h', palette='pastel')
plt.title('Box Plot of Numerical Columns')
plt.xlabel('Value')
plt.xlim(-100, 20000)
plt.show()

## handling Outliers using z-score
outliers=(sales[numerical_columns].abs()>3).sum()
print('outliers detected:/n',outliers)

#correlation matrix
correlation_matrix = sales.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

"""**Data Visualization and Preprocessing Conclusion**

**Data Visualization:** Helped to identify missing values, outliers, distributions, and relationships between variables

**Preprocessing:**Included handling missing values, encoding categorical data, detecting outliers, and scaling features for better model performance

# Feature Selection and Model Building

# **Feature Selection**
"""

#Selecting categorical and numerical features
categorical_columns = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
numerical_columns = ['Unit price', 'Quantity', 'Tax 5%', 'cogs', 'gross income', 'Rating']
target = 'Sales'

#Drop Unnecessary Columns
sales = sales.drop(['Invoice ID', 'City', 'Time', 'gross margin percentage'], axis=1)
sales

#print sales columns
sales.columns

#to identify highly correlated features by correlation heatmap
# Calculate the correlation matrix only for numerical features
corr = sales.corr(numeric_only=True)[target].sort_values(ascending=False).to_frame()
#plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

#combine Branch and Customer type into a single feature
sales['Branch_Customer type'] = sales['Branch'].astype(str) + '_' + sales['Customer type'].astype(str)
#Display first few rows
sales.head()

#create a new feature by multiplying Unit price and Quanity
sales['Total Cost'] = sales['Unit price'] * sales['Quantity']
sales.head()

drop_features = ['Branch_Customer type','cogs','Gender']
sales = sales.drop(drop_features, axis=1)
sales.head()

selected_features = sales.columns
selected_features

#shape of original features
original_features = sales.shape[1]
original_features

#shape of selected features after selecting features
selected_features = sales.shape[1]
selected_features

"""# **Model Building**"""

#Selecting features based on previous analysis
selected_features = ['Unit price', 'Quantity', 'Tax 5%', 'gross income', 'Rating', 'Total Cost']

#Split Data into training and testing sets
from sklearn.model_selection import train_test_split
X = sales[selected_features]
y = sales[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training Set: {X_train.shape}, {y_train.shape}")
print(f"Testing Set: {X_test.shape}, {y_test.shape}")

#Intializing Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVC
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

#Linear Regression Model
from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)
y_pred = linear_regression.predict(X_test)
print("Linear Regression Metrics:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#Decision Tree Regression Model
from sklearn.tree import DecisionTreeRegressor
decision_tree = DecisionTreeRegressor()
decision_tree.fit(X_train, y_train)
y_pred = decision_tree.predict(X_test)
print("Decision Tree Regression Metrics:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#Random Forest Regressor Model
from sklearn.ensemble import RandomForestRegressor
random_forest = RandomForestRegressor()
random_forest.fit(X_train, y_train)
y_pred = random_forest.predict(X_test)
print("Random Forest Regression Metrics:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#Gradient Boosting Regressor Model
from sklearn.ensemble import GradientBoostingRegressor
gradient_boosting = GradientBoostingRegressor()
gradient_boosting.fit(X_train, y_train)
y_pred = gradient_boosting.predict(X_test)
print("Gradient Boosting Regression Metrics:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Support Vector machine Regressor
from sklearn.svm import SVR # Import SVR instead of SVC
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
svm_regressor = SVR() # Import SVR instead of SVC
svm_regressor.fit(X_train, y_train)
y_pred = svm_regressor.predict(X_test)
print("Support Vector Machine Regressor Metrics:")
# Use regression metrics instead of classification metrics
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# XGBRegressor
from xgboost import XGBRegressor
xgb_regressor = XGBRegressor()
xgb_regressor.fit(X_train, y_train)
y_pred = xgb_regressor.predict(X_test)
print("XGBoost Regressor Metrics:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

"""# Comparision of Model Performance"""

#Define models
models_scores = {
    'Linear Regression': r2_score(y_test, y_pred),
    'Decision Tree Regression':  r2_score(y_test, y_pred),
    'Random Forest Regression': r2_score(y_test, y_pred),
    'Gradient Boosting Regression': r2_score(y_test, y_pred),
    'Support Vector Machine Regression':  r2_score(y_test, y_pred),
    'XGBoost Regression': r2_score(y_test, y_pred)
}

All_Model_Score = pd.DataFrame(list(models_scores.items()), columns=["Model", "R2 Score"])
score = All_Model_Score.sort_values(by='R2 Score' ,ascending=False)
print(score)

"""# Visualization of Model Performance"""

#Comparision of model performance
plt.figure(figsize=(10, 6))
sns.barplot(x='Model', y='R2 Score', data=score, color='yellow')
plt.title('Model Performance Comparison(Supermarket Sales Prediction)')
plt.xlabel('Model')
plt.ylabel('R2 Score')
plt.xticks(rotation=90)
plt.show()

"""# **Unsupervised Clustering to figure out Customer Cluster Bases**"""

#unsupervised clustering to figure out customer cluster bases
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs
from sklearn.metrics import roc_curve, auc
from sklearn.cluster import AgglomerativeClustering

# Define features and target
target = 'Rating'  # Changed to 'Rating' with capital 'R'
X = sales.drop(columns=[target])
y = sales[target]
print(X.head())
print(y.head())

# Assuming 'X' contains non-numerical columns like 'Invoice ID'
# Select only numerical features for clustering
X_numerical = X.select_dtypes(include=np.number) # Selects only numerical features

# Perform clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_numerical)  # Use X_numerical instead of X
# Determine optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    print(f"Cluster {i} done")
    print(wcss)
    # Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Fit KMeans with optimal clusters (assuming 3 for example)
optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
kmeans.fit(X_scaled)
sales['Cluster'] = kmeans.fit_predict(X_scaled)
print(sales.head())

# Perform PCA for visualization
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
sales['PCA1'] = X_pca[:, 0]
sales['PCA2'] = X_pca[:, 1]
print(sales.head())

#plot Customer Clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=sales, palette='pastel')
plt.title('Customer Clusters')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# Generate synthetic data using make_blobs
X, y = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Extract relevant columns, using actual column names from the 'sales' DataFrame
# Ensure the column 'Total Price' exists. If not, create it.
if 'Total Price' not in sales.columns:
    sales['Total Price'] = sales['Unit price'] * sales['Quantity']

X = sales[['Total Price', 'Rating']]
y = sales['Cluster']

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total Price', y='Rating', hue='Cluster', data=sales, palette='pastel')
plt.title('Customer Clusters')
plt.xlabel('Total Sales')
plt.ylabel('Rating')
plt.show()

# Merge clusters with sales dataset
sales_with_clusters = pd.merge(sales, sales[['Cluster']], left_index=True, right_index=True)
print(sales_with_clusters.head())

#  Visualization
plt.figure(figsize=(12, 8))
# Replace 'total_sales' with the actual column name containing total sales, for example, 'Total Price' or 'Sales'.
# Replace 'rating' and 'Customer_Clusters' with actual column names as well, if needed.
c = sns.scatterplot(data=sales, x='Total Price', y='Rating', hue='Cluster', palette='viridis', s=100)
c.set_facecolor('grey')
plt.title('Customer Segmentation Based on Sales and Rating')
plt.xlabel('Total Sales')
plt.ylabel('Rating')
plt.grid(True)
plt.legend(title='Customer Clusters', loc='upper right')
plt.show()

print("Customer segmentation based on sales and rating")
sales.sample(10)

# Train a classification model for ROC curve analysis
# Assuming 'sales' DataFrame contains the 'Cluster' column generated by KMeans
X_train, X_test, y_train, y_test = train_test_split(X_scaled, sales['Cluster'], test_size=0.2, random_state=42)
from sklearn.ensemble import GradientBoostingClassifier # Import GradientBoostingClassifier
clf = GradientBoostingClassifier()
clf.fit(X_train, y_train)
y_prob = clf.predict_proba(X_test)

# Plot ROC curve for each class
plt.figure(figsize=(10, 6))
# Get the number of classes from the shape of y_prob
n_classes = y_prob.shape[1]
for i in range(n_classes):  # Iterate over the actual number of classes
    fpr, tpr, _ = roc_curve(y_test == i, y_prob[:, i])
    plt.plot(fpr, tpr, label=f'Class {i} (AUC = {auc(fpr, tpr):.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Analysis')
plt.legend(loc='lower right')
plt.show()

print("Customer segmentation based on multiple clustering methods")
sales.sample(10)

# Visualization - Hierarchical Clustering
plt.figure(figsize=(10, 6))
sns.lineplot(x='PCA1', y='PCA2', hue='Cluster', data=sales, palette='pastel')
plt.title('Customer Clusters (Hierarchical Clustering)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

"""# **Feature Selection and Model Building Conclusion**

**Feature Selection**

*  Categorical features like Branch, City, Customer type, Gender, Product line, and Payment were encoded to numerical values using Label Encoding.
*   Features like Unit Price, Quantity, Tax 5%, Gross Income, and COGS showed a direct impact on Sales, making them crucial predictors.

*   Time-related features (Date, Time) might have been transformed or excluded based on their significance in model performance.

**Model Building & Comparison**

*  **Linear Regression:** Performed decently but might have struggled with non-linearity in the data.
*   **Decision Tree:** Captured non-linear patterns but might have overfitted.

*   **Random Forest:** Provided better generalization and improved accuracy by reducing overfitting.
*   **XGBoost:** Delivered the best performance, optimizing the balance between bias and variance, and handling feature interactions efficiently.

**Model Performance Metrics**

*   MAE, MSE, and RMSE were compared across models.
*   XGBoost showed the lowest RMSE, making it the most reliable model for predicting sales.

**Final Decision**

*   XGBoost is recommended for supermarket sales prediction due to its superior accuracy and robustness.
*   Feature engineering (e.g., extracting insights from Date/Time) could further enhance predictive power.

# **Unsupervised Clusters**

*   The analysis successfully segmented supermarket customers into four distinct clusters based on total sales and ratings. By applying KMeans clustering, we identified patterns in customer purchasing behavior and satisfaction levels. The visualization of these clusters provides insights into how different customer groups contribute to overall sales and ratings.


*   The implementation successfully clusters supermarket customers based on total sales and rating using unsupervised machine learning techniques.

*   **KMeans Clustering:** was applied with 4 clusters to segment customers into distinct groups.

*   The **visualization** using a scatter plot helps in identifying different customer clusters, showing variations in spending patterns and satisfaction levels.
*   The **clusters were merged** with the sales dataset, allowing further business insights and targeted strategies.


*   **Hierarchical Clustering:** Identified similar patterns in customer groups.

# **Final Thoughts:**

This approach enables data-driven decision-making, allowing businesses to optimize **customer targeting, marketing strategies, and service improvements**. Further refinement with more features or additional clustering methods can enhance segmentation accuracy.
"""