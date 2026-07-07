from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.rol import RolCreate, RolResponse
from app.models.rol import Rol

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/", response_model=RolResponse)
def create_rol(rol: RolCreate, db:Session = Depends(get_db), current_user = Depends(get_current_user)):
    new_rol = Rol(rol_name=rol.rol_name, feature=rol.feature)
    db.add(new_rol)
    db.commit()
    db.refresh(new_rol)
    return new_rol