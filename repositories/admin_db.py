from models.admin_model import Admin


def get_admin_db_all(db, skip, limit):
    admin = db.query(Admin).offset(skip).limit(limit).all()
    return admin


def get_admin_db_by_id(db, ID):
    admin_id = db.query(Admin).filter(Admin.id == ID).first()
    return admin_id


def new_admin_db(new_admin, db):
    admin_item = db.query(Admin).filter(Admin.user_name == new_admin.user_name).first()
    return admin_item
