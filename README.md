# SquatGym AI Expense Engine 🏋️‍♂️📊

> Automated Third-Party Expense Auditing & Executive PDF Reporting API for Gym Chains.

Branch managers spend over 3 hours every month manually auditing third-party supplier receipts (sanitation, equipment maintenance, utilities) and generating executive PDF reports. 
**SquatGym AI Expense Engine** automates invoice text parsing via LLMs, PostgreSQL persistence, and ReportLab PDF export in under **10 seconds** (1080x speedup).

| Concept | Status | Implementation Details |
| :--- | :--- | :--- |
| **API Endpoints** | ✅ Implemented | RESTful FastAPI routes with Pydantic body validation and strict HTTP status codes. |
| **Database** | ✅ Implemented | PostgreSQL 15 managed via SQLModel / SQLAlchemy ORM. |
| **Authentication** | ✅ Implemented | Protected routes guarded by Supabase Auth JWT Bearer dependencies. |
| **Reporting (PDF)** | ✅ Implemented | Binary PDF executive financial summary generated via ReportLab. |
| **LLM Integration** | ✅ Implemented | Narrow AI task parsing unstructured raw receipt text into structured JSON data. |
| **Containerized Stack** | 🔄 Swapped | Full stack (API + PostgreSQL DB) launched via `docker compose up`. |

---


### 1. Clone & Set Environment
```bash
git clone [https://github.com/tu-usuario/squatgym-expense-engine.git](https://github.com/tu-usuario/squatgym-expense-engine.git)
cd squatgym-expense-engine
cp .env.example .env