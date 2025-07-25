# KPA Backend Assignment - FastAPI Implementation

## 🔧 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite (via SQLAlchemy ORM)
- **Language**: Python 3.10+
- **API Documentation**: Swagger UI (`/docs`)

---

## 📋 Implemented APIs

Implemented two API endpoints each for **Bogie** and **Wheel** forms based on the provided Postman collection.

### 🚆 Bogie Form

- `POST /api/forms/`

  - **Payload**: `{ "name": "string", "part_number": "string" }`
  - **Function**: Creates a new bogie form entry.

- `GET /api/forms/`

  - **Function**: Fetches all bogie form entries.

### 🛞 Wheel Form

- `POST /api/forms/wheel/`

  - **Payload**: `{ "inspector_name": "string", "wheel_number": "string" }`
  - **Function**: Creates a new wheel form entry.

- `GET /api/forms/wheel/`

  - **Function**: Fetches all wheel form entries.

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-link>
cd <repo-folder>
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
uvicorn main:app --reload
```

5. **Access the API Docs**

- Navigate to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📂 Folder Structure

```
.
├── main.py              # Entry point for FastAPI app
├── database.py          # DB connection and Base setup
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic request/response schemas
├── formdata.py          # API routes logic for Bogie and Wheel forms
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📌 Assumptions & Notes

- SQLite used for simplicity; can be swapped with PostgreSQL easily.
- Minimal error handling implemented (FastAPI auto-validates schema).
- Authentication was not implemented, per assignment focus.

---

## 📹 Project Walkthrough

👉 Video Demo: https://drive.google.com/file/d/1pFtyGru9VeEjZ9BAze6654pUrrkvd4RY/view?usp=sharing

---

## 📬 Contact

**Aman Chaurasia**\
Email: [aman007chaurasia@gmail.com](mailto\:aman007chaurasia@gmail.com)\
GitHub: [@aman18Chaurasia](https://github.com/aman18Chaurasia)\
LinkedIn: [@aman-chaurasia](https://www.linkedin.com/in/aman-chaurasia-91443b263)

