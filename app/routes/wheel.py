from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import WheelForm
from app.schemas import WheelFormCreate
from app.formdata import get_db

router = APIRouter()

@router.post("/", status_code=201)
def create_wheel_form(form: WheelFormCreate, db: Session = Depends(get_db)):
    new_form = WheelForm(**form.dict())
    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return new_form

@router.get("/")
def read_wheel_forms(db: Session = Depends(get_db)):
    return db.query(WheelForm).all()
