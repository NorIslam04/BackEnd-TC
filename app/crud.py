from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_admin(db: Session, admin: schemas.Admin):
    existing_admin = db.query(models.Admin).filter(models.Admin.username == admin.username).first()
    if existing_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    admin = models.Admin(username=admin.username, password=hash_password(admin.password))
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def get_employe(db: Session):
    return db.query(models.Employe).all()

def get_RH(db: Session):
    return db.query(models.RessourceHumaine).all()

def get_tache(db: Session):
    return db.query(models.Tache).all()

def get_employe_tache(db: Session):
    return db.query(models.EmployeTache).all()

def get_historique(db: Session):
    return db.query(models.Historique).all()