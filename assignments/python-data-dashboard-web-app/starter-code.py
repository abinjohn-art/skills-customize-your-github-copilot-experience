from fastapi import FastAPI
import pandas as pd

app = FastAPI()

def load_data():
    df = pd.read_csv("sales_data.csv")
    df["revenue"] = df["price"] * df["quantity"]
    return df

sales_df = load_data()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Python Data Dashboard Web App"}

@app.get("/summary")
def summary():
    total_rows = len(sales_df)
    total_revenue = float(sales_df["revenue"].sum())
    total_quantity = int(sales_df["quantity"].sum())
    return {
        "total_rows": total_rows,
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
    }

@app.get("/top-product")
def top_product():
    top = sales_df.groupby("product")["revenue"].sum().idxmax()
    top_revenue = float(sales_df.groupby("product")["revenue"].sum().max())
    return {"top_product": top, "top_revenue": top_revenue}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
