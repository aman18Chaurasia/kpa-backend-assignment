# KPA Backend Assignment

Follow the README steps to run this FastAPI project.
# KPA Backend Assignment

## 🚀 Setup Instructions

```bash
git clone <your-repo-url>
cd kpa_backend_assignment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Update credentials in .env
uvicorn app.main:app --reload
🛠️ Tech Stack
FastAPI

PostgreSQL

SQLAlchemy

Pydantic

Uvicorn

📌 APIs Implemented
1. Root Endpoint
GET / – returns a health check JSON

2. Bogie Form
POST /api/forms/bogie/

GET /api/forms/bogie/

3. Wheel Form
POST /api/forms/wheel/

GET /api/forms/wheel/

📎 Assumptions & Limitations
Only basic validation has been implemented.

No authentication layer included.

DB schema assumes direct insert of data without relations for simplicity.
