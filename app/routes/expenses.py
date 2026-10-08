from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session, select
from typing import List
from app.core.database import get_session
from app.core.auth import get_current_user
from app.models.expense import Expense, ExpenseCreate
from app.services.llm_auditor import parse_raw_receipt_with_llm
from app.services.pdf_generator import build_expense_pdf_report

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/audit-raw", response_model=Expense, status_code=status.HTTP_201_CREATED)
def audit_and_create_expense(
    raw_text: str,
    session: Session = Depends(get_session),
    user = Depends(get_current_user)
):
    parsed_data = parse_raw_receipt_with_llm(raw_text)
    user_email = user.get("email") if isinstance(user, dict) else user.email
    
    new_expense = Expense(
        supplier_name=parsed_data["supplier"],
        category=parsed_data["category"],
        amount=parsed_data["amount"],
        tax_id=parsed_data["tax_id"],
        created_by=user_email
    )
    session.add(new_expense)
    session.commit()
    session.refresh(new_expense)
    return new_expense

@router.get("/", response_model=List[Expense])
def list_expenses(session: Session = Depends(get_session), user = Depends(get_current_user)):
    return session.exec(select(Expense)).all()

@router.get("/export-pdf")
def export_pdf_report(session: Session = Depends(get_session), user = Depends(get_current_user)):
    expenses = session.exec(select(Expense)).all()
    user_email = user.get("email") if isinstance(user, dict) else user.email
    pdf_bytes = build_expense_pdf_report(expenses, user_email)
    
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=SquatGym_Expense_Report.pdf"}
    )