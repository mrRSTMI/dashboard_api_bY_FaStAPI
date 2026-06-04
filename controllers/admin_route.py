from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas.admin_schema import ResponseAdmin, NewAdmin, UpdateAdmin
from models.admin_model import Admin
from core.database import get_db
from services.admin_service import (
    get_admin_service_by_id,
    get_admin_service,
    new_admin_service,
    update_admin_service,
    delete_admin_service,
)

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.get("/", response_model=list[ResponseAdmin])
async def get_admin(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_admin_service(db=db, skip=skip, limit=limit)


@router.get("/{ID}", response_model=ResponseAdmin)
async def get_admin_by_id(ID: int, db: Session = Depends(get_db)):
    return get_admin_service_by_id(ID=ID, db=db)


@router.post("/new-admin", response_model=ResponseAdmin)
async def new_admin(new_admin: NewAdmin, db: Session = Depends(get_db)):
    return new_admin_service(new_admin=new_admin, db=db)


@router.put("/update-admin/{ID}", response_model=ResponseAdmin)
async def update_admin_by_id(
    ID: int, update_admin: UpdateAdmin, db: Session = Depends(get_db)
):
    return update_admin_service(db=db, update_admin=update_admin, ID=ID)


@router.delete("/delete-admin/{ID}")
async def delelte_admin_by_id(ID: int, db: Session = Depends(get_db)):
    return delete_admin_service(ID=ID, db=db)
