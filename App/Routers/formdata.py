from fastapi import APIRouter, HTTPException
from app.schemas import FormData
from app.models import fake_db

router = APIRouter(prefix="/api/v1/formdata", tags=["Form Data"])

@router.post("")
def submit_formdata(form: FormData):
    new_id = len(fake_db) + 1
    fake_db[new_id] = form.dict()
    return {"id": new_id, "message": "Form submitted successfully"}

@router.get("/{form_id}")
def get_formdata(form_id: int):
    if form_id in fake_db:
        return {"id": form_id, "data": fake_db[form_id]}
    raise HTTPException(status_code=404, detail="Form not found")
