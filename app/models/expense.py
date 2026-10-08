from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    supplier_name: str
    category: str
    amount: float
    tax_id: str
    created_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ExpenseCreate(SQLModel):
    supplier_name: str
    category: str
    amount: float
    tax_id: str