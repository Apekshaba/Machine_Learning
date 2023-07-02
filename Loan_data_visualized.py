# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:27:32 2020

@author: GOHIL
"""
#Importing necessary libraries and packages:
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math as m

data=pd.read_excel("loan.xlsx")
data
data.head()
pd.set_option("display.max_columns",200) 
data.head()
data.info()
data.shape[0]
data.shape[1]
data.describe()

#Creating a data frame with only numeric features for visualizations:
num_cols=['loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','inq_last_6mths','revol_bal','revol_util']
#Scrutizing the numeric features for missing values:
data[num_cols].head()
data[num_cols].info() #Feature revol_util has 50 missing values. Temporarily left untreated.
num_cols=['loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','inq_last_6mths','revol_bal']

#Histogram visualizations of numeric data:
def plot_density_hist(data,cols):
    for col in cols:
        sns.set_style("whitegrid")
        sns.distplot(data[col],bins=30,rug=True,hist=True)
        plt.title('Histogram of -'+col)
        plt.xlabel('col->')
        plt.ylabel('No. of customers')
        plt.show()      
plot_density_hist(data,num_cols)
#Histogram visualizations of numeric data:
num_cols2=['open_acc','total_acc','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int','total_rec_late_fee','last_pymnt_amnt']
def plot_density_hist(data,cols):
    for col in cols:
        sns.set_style("whitegrid")
        sns.distplot(data[col],bins=30,rug=True,hist=True)
        plt.title('Histogram of -'+col)
        plt.xlabel('col->')
        plt.ylabel('No. of customers')
        plt.show()      
plot_density_hist(data,num_cols2)
#Bi-variate analysis by box-plots and violin-plots:
def plot_box(data, cols, col_x = 'loan_status'):
    for col in cols:
        sns.set_style("whitegrid")
        sns.boxplot(col_x, col, data=data)
        plt.xlabel(col_x) # Set text for the x axis
        plt.ylabel(col)# Set text for y axis
        plt.show()
num_cols3=num_cols+num_cols2
num_cols3
plot_box(data, num_cols)
sns.boxplot(data['loan_status'],data['loan_amnt'],data=data)

def plot_violin(data, cols, col_x = 'loan_status'):
    for col in cols:
        sns.set_style("whitegrid")
        sns.violinplot(col_x, col, data=data)
        plt.xlabel(col_x) # Set text for the x axis
        plt.ylabel(col)# Set text for y axis
        plt.show()
num_cols3=num_cols+num_cols2
num_cols3
plot_violin(data, num_cols)
sns.boxplot(data['loan_status'],data['loan_amnt'],data=data)

#Scatter plot visualizations:
def scatter(data, cols, shape_col='loan_status', col_y='loan_amnt',alpha=0.2):
    shapes = ['+','o','^']
    unique_cats=data[shape_col].unique()
    for col in cols:
        sns.set_style("whitegrid")
        for i, cat in enumerate(unique_cats):
            temp=data[data[shape_col]==cat]
            sns.regplot(col,col_y,data=temp,marker=shapes[i],label=cat,scatter_kws={"alpha":alpha},fit_reg=False,color='blue')
            plt.title("Scatter plot of "+col_y+"VS"+col)
            plt.xlabel(col)
            plt.ylabel(col_y)
            plt.legend()
            plt.show()
    
scatter(data,num_cols3)

def cond_plot_loanamnt(cols):
    import IPython.html.widgets
    import seaborn as sns
    for col in cols:
        g = sns.FacetGrid(data, col="loan_status",row='inq_last_6mths',hue="loan_status", palette="Set2", margin_titles=True)
        g.map(sns.regplot, col, "loan_amnt", fit_reg = False)


cond_plot_loanamnt(num_cols3)   
def cond_plot_annualinc(cols):
    import IPython.html.widgets
    import seaborn as sns
    for col in cols:
        g = sns.FacetGrid(data, col="loan_status",row='inq_last_6mths',hue="loan_status", palette="Set2", margin_titles=True)
        g.map(sns.regplot, col, "annual_inc", fit_reg = False)


cond_plot_annualinc(num_cols3) 
fig=plt.figure(figsize=(20,20))
sns.boxplot(data['loan_status'],data['acc_now_delinq'],data=data)
fig=plt.figure(figsize=(20,20))
sns.boxplot(data['purpose'],data['loan_amnt'],data=data)
fig=plt.figure(figsize=(20,20))
sns.boxplot(data['purpose'],data['int_rate'],data=data)
fig=plt.figure(figsize=(20,20))
sns.boxplot(data['purpose'],data['inq_last_6mths'],data=data)
data["delinq_2yrs"].value_counts()
sns.boxplot(data['loan_status'],data['total_pymnt'],data=data)
