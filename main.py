from fastapi import FastAPI
from app.core.database import init_db
from app.routes import expenses

app = FastAPI(
    title="SquatGym AI Expense Engine",
    version="1.0.0",
    description="Backend Capstone API for Automated Third-Party Expense Auditing & PDF Reporting"
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(expenses.router)

@app.get("/")
def root():
    return {"status": "ok", "system": "SquatGym AI Expense Engine"}