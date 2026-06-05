from models.admin_model import Admin
from fastapi import HTTPException
from repositories.admin_db import get_admin_db_all, get_admin_db_by_id, new_admin_db


def get_admin_service(db, skip, limit):
    admin = get_admin_db_all(
        db=db,
        skip=skip,
        limit=limit,
    )
    return admin


def get_admin_service_by_id(db, ID):
    admin_id = get_admin_db_by_id(db, ID)
    if not admin_id:
        raise HTTPException(status_code=404, detail=f" === id {ID} is not found === ")
    if admin_id:
        return admin_id


def new_admin_service(new_admin, db):
    admin_item = new_admin_db(new_admin, db)
    if admin_item:
        raise HTTPException(
            status_code=406, detail=f" * * * === your admin is exist === * * *"
        )
    # if not admin_item:
    #     admin_new = Admin(
    #         name_admin=new_admin.name_admin,
    #         email=new_admin.email,
    #         user_name=new_admin.user_name,
    #         password=new_admin.password,
    #         is_write=new_admin.is_write,
    #         changer_access=new_admin.changer_access,
    #     )
    admin_new = Admin(**new_admin.model_dump())
    db.add(admin_new)
    db.commit()
    db.refresh(admin_new)
    return admin_new


def update_admin_service(db, update_admin, ID):
    admin_item = get_admin_db_by_id(db, ID)
    if not admin_item:
        raise HTTPException(status_code=404, detail=f" === id {ID} is not found === ")

    new_update_admin = update_admin.model_dump(exclude_unset=True)
    for key, value in new_update_admin.items():
        setattr(admin_item, key, value)
    print(type(admin_item))
    print(update_admin.model_dump())

    db.commit()
    db.refresh(admin_item)
    return admin_item


def delete_admin_service(db, ID):
    admin_item = get_admin_db_by_id(db, ID)
    if not admin_item:
        raise HTTPException(status_code=404, detail=f" === id {ID} is not found === ")
    if admin_item:
        db.delete(admin_item)
        db.commit()
        return {"message": f" === admin by {ID} is deleted === "}
