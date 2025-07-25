from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import BogieForm
from app.schemas import BogieFormCreate
from app.formdata import get_db

router = APIRouter()

@router.post("/", status_code=201)
def create_bogie_form(form: BogieFormCreate, db: Session = Depends(get_db)):
    new_form = BogieForm(**form.dict())
    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return new_form

@router.get("/")
def read_bogie_forms(db: Session = Depends(get_db)):
    return db.query(BogieForm).all()
