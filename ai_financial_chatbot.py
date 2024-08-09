# -*- coding: utf-8 -*-
"""AI-Financial-Chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/141Ou3vUzMwYGOHEgzo4DlnDSX_NJWgGD
"""

import csv
import pandas as pd

# Load financial data from CSV file
df = pd.read_csv('Financial_Data.csv')

# Define predefined queries and responses
queries = {
    "What is the total revenue?": lambda company: f"The total revenue for {company} is ${df.loc[df['Company'] == company, 'Revenue'].values[0]}.",
    "What is the net income?": lambda company: f"The net income for {company} is ${df.loc[df['Company'] == company, 'Net_income'].values[0]}.",
    "What are the total assets?": lambda company: f"The total assets for {company} are ${df.loc[df['Company'] == company, 'total_assets'].values[0]}.",
    "What are the total liabilities?": lambda company: f"The total liabilities for {company} are ${df.loc[df['Company'] == company, 'total_lib'].values[0]}.",
    "What is the operating cash flow?": lambda company: f"The operating cash flow for {company} is ${df.loc[df['Company'] == company, 'cashflow_operating'].values[0]}.",
    "What is the debt-to-equity ratio?": lambda company: get_debt_to_equity_ratio(df, company),
    "What is the return on assets (ROA)?": lambda company: get_roa(df, company),
    "What is the return on equity (ROE)?": lambda company: get_roe(df, company),
    "What is the current ratio?": lambda company: get_current_ratio(df, company),
    "What is the profit margin?": lambda company: get_profit_margin(df, company)
}

def get_net_income(df, company):
    current_year = df.loc[df['Company'] == company, 'Fiscal_year'].max()
    net_income = df.loc[(df['Company'] == company) & (df['Fiscal_year'] == current_year), 'Net_income'].values[0]
    return f"The net income for {company} in {current_year} is ${net_income}."

def get_net_income_change(df, company):
    current_year = df.loc[df['Company'] == company, 'Fiscal_year'].max()
    previous_year = current_year - 1
    current_net_income = df.loc[(df['Company'] == company) & (df['Fiscal_year'] == current_year), 'Net_income'].values[0]
    previous_net_income = df.loc[(df['Company'] == company) & (df['Fiscal_year'] == previous_year), 'Net_income'].values[0]
    change = current_net_income - previous_net_income
    if change > 0:
        return f"The net income for {company} has increased by ${change} from {previous_year} to {current_year}."
    else:
        return f"The net income for {company} has decreased by ${abs(change)} from {previous_year} to {current_year}."

def get_debt_to_equity_ratio(df, company):
    total_liability = df.loc[df['Company'] == company, 'total_lib'].values[0]
    total_assets = df.loc[df['Company'] == company, 'total_assets'].values[0]
    equity = total_assets - total_liability
    debt_to_equity_ratio = total_liability / equity
    return f"The debt-to-equity ratio for {company} is {debt_to_equity_ratio:.2f}."

def get_roa(df, company):
    net_income = df.loc[df['Company'] == company, 'Net_income'].values[0]
    total_assets = df.loc[df['Company'] == company, 'total_assets'].values[0]
    roa = (net_income / total_assets) * 100
    return f"The return on assets (ROA) for {company} is {roa:.2f}%."

def get_roe(df, company):
    net_income = df.loc[df['Company'] == company, 'Net_income'].values[0]
    total_liability = df.loc[df['Company'] == company, 'total_lib'].values[0]
    total_assets = df.loc[df['Company'] == company, 'total_assets'].values[0]
    equity = total_assets - total_liability
    roe = (net_income / equity) * 100
    return f"The return on equity (ROE) for {company} is {roe:.2f}%."

def get_current_ratio(df, company):
    total_assets = df.loc[df['Company'] == company, 'total_assets'].values[0]
    total_liability = df.loc[df['Company'] == company, 'total_lib'].values[0]
    current_ratio = total_assets / total_liability
    return f"The current ratio for {company} is {current_ratio:.2f}."

def get_profit_margin(df, company):
    revenue = df.loc[df['Company'] == company, 'Revenue'].values[0]
    net_income = df.loc[df['Company'] == company, 'Net_income'].values[0]
    profit_margin = (net_income / revenue) * 100
    return f"The profit margin for {company} is {profit_margin:.2f}%."

# Chatbot loop
while True:
    user_input = input("Enter your query: ")
    company = input("Enter the company name: ")
    if user_input in queries:
        print(queries[user_input](company))
    else:
        print("Sorry, I didn't understand your query. Please try again!")

# import pandas as pd
# import numpy as np
# import transformers
# # The accuracy_score function is not suitable for this task and has been removed
# # from sklearn.metrics import accuracy_score

# # Load financial data from CSV file
# df = pd.read_csv('Financial_Data.csv')

# # Define predefined queries and responses
# queries = {
#     "What is the total revenue?": lambda company: f"The total revenue for {company} is ${df.loc[df['Company'] == company, 'Revenue'].values[0]}.",
#     "What is the net income?": lambda company: f"The net income for {company} is ${df.loc[df['Company'] == company, 'Net_income'].values[0]}.",
#     "What are the total assets?": lambda company: f"The total assets for {company} are ${df.loc[df['Company'] == company, 'total_assets'].values[0]}.",
#     "What are the total liabilities?": lambda company: f"The total liabilities for {company} are ${df.loc[df['Company'] == company, 'total_lib'].values[0]}.",
#     "What is the operating cash flow?": lambda company: f"The operating cash flow for {company} is ${df.loc[df['Company'] == company, 'cashflow_operting'].values[0]}."
# }

# # Removed the calculate_accuracy function as it is not applicable here

# # Define a function to generate responses using NLP and Machine Learning
# def generate_response(query, company):
#     nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
#     chat = nlp(transformers.Conversation(query), pad_token_id=50256)
#     response = str(chat)
#     response = response[response.find("bot >> ")+6:].strip()
#     return response

# # Define a function to check if the response is related to the question
# def is_response_related(query, response):
#     # Use a simple keyword matching approach for demonstration purposes
#     keywords = ["revenue", "income", "assets", "liabilities", "cash flow"]
#     if any(keyword in query.lower() for keyword in keywords) and any(keyword in response.lower() for keyword in keywords):
#         return True
#     return False

# # Chatbot loop
# while True:
#     user_input = input("Enter your query: ")
#     company = input("Enter the company name: ")
#     if user_input in queries:
#         response = queries[user_input](company)
#     else:
#         response = generate_response(user_input, company)

#     # Removed accuracy calculation and print statements

#     # Check if the response is related to the question
#     if is_response_related(user_input, response):
#         print("Response is related to the question.")
#     else:
#         print("Response is not related to the question.")

#     print(response)

