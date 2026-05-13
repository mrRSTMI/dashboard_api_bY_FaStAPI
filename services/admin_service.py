from models.admin_model import Admin
from fastapi import HTTPException

def get_admin_service(db,skip,limit):
    admin = db.query(Admin).offset(skip).limit(limit).all()
    return admin

def get_admin_service_by_id(db,ID):
    admin_id = db.query(Admin).filter(Admin.id == ID).first()
    if not admin_id:
       raise HTTPException(status_code=404, detail=f" === id {ID} is not found === ")
    if admin_id:
        return admin_id
    

def new_admin_service(new_admin , db):
    admin_item = db.query(Admin).filter(Admin.user_name == new_admin.user_name).first()
    if admin_item:
        raise HTTPException(status_code=406, detail=f" * * * === your admin is exist === * * *")
    if not admin_item:
        admin_new = Admin(name_admin = new_admin.name_admin, email = new_admin.email, user_name = new_admin.user_name, password = new_admin.password, is_write = new_admin.is_write, changer_access = new_admin.changer_access)
        db.add(admin_new)
        db.commit()
        db.refresh(admin_new)
        return new_admin
    
def update_admin_service(db, update_admin, ID):
    admin_item = db.query(Admin).filter(Admin.id == ID).first()

    if not admin_item:
        raise HTTPException(status_code=404, detail=f" === id {ID} is not found === ")
    
    if update_admin.name_admin is not None:
        admin_item.name_admin = update_admin.name_admin

    if update_admin.email is not None:
        admin_item.email = update_admin.email

    if update_admin.user_name is not None:
        admin_item.user_name = update_admin.user_name

    if update_admin.password is not None:
        admin_item.password = update_admin.password

    if update_admin.is_write is not None:
        admin_item.is_write = update_admin.is_write

    if update_admin.changer_access is not None:
        admin_item.changer_access = update_admin.changer_access
    

    db.commit()
    db.refresh(admin_item)
    return admin_item

def delete_admin_service(db,ID):
    admin_item = db.query(Admin).filter(Admin.id == ID).first()
    if not admin_item:
        raise HTTPException(status_code=404, detail=f" === id {ID} is not found === ")
    if admin_item:
        db.delete(admin_item)
        db.commit()
        return {"message":f" === admin by {ID} is deleted === "}