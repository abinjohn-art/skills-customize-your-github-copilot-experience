# 📘 Assignment: Python Data Dashboard Web App

## 🎯 Objective

Build an integrated Python project that loads and explores a dataset, then exposes key insights through a simple FastAPI web API.

## 📝 Tasks

### 🛠️ Load and Explore the Dataset

#### Description
Use pandas to load the provided sales dataset and explore its contents.

#### Requirements
Completed program should:

- Load `sales_data.csv` into a pandas DataFrame
- Print the first 5 rows and basic summary statistics
- Compute total revenue and total quantity sold


### 🛠️ Create a FastAPI Web API

#### Description
Set up a FastAPI application with a root endpoint and a JSON response.

#### Requirements
Completed program should:

- Initialize a FastAPI app in `starter-code.py`
- Add a root endpoint `/` that returns a welcome message
- Run locally with Uvicorn


### 🛠️ Connect Data to the API

#### Description
Create API endpoints that return summary information derived from the dataset.

#### Requirements
Completed program should:

- Load the dataset when the app starts
- Add an endpoint `/summary` that returns total rows, total revenue, and total quantity
- Add an endpoint `/top-product` that returns the product with the highest revenue
