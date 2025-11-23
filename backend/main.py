from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load mock account data
with open("mock_accounts.json") as f:
    accounts = json.load(f)

@app.get("/balance/{account_id}")
def get_balance(account_id: str):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_id": account_id, "balance": accounts[account_id]["balance"]}

@app.get("/transactions/{account_id}")
def get_transactions(account_id: str):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_id": account_id, "transactions": accounts[account_id]["transactions"]}

@app.post("/transfer")
def transfer_funds(from_id: str, to_id: str, amount: float):
    if from_id not in accounts or to_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    if accounts[from_id]["balance"] < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    accounts[from_id]["balance"] -= amount
    accounts[to_id]["balance"] += amount
    return {"message": f"Transferred {amount} from {from_id} to {to_id}"}
