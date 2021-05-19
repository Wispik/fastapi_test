from sqlalchemy.orm import Session

import schemas
from database import models


def get_languages(db: Session):
    return db.query(models.Language).all()


def get_language(db: Session, lang_id: int):
    return db.query(models.Language).filter(models.Language.id == lang_id).first()


def create_language(db: Session, lang: schemas.LanguageBase):
    db_lang = models.Language(**lang.dict())
    db.add(db_lang)
    db.commit()
    return db_lang


def delete_language(db: Session, lang_id: int):
    db_del = db.query(models.Language).filter(models.Language.id == lang_id).delete()
    db.commit()
    return db_del


def update_language(db: Session, lang_id: int, lang: schemas.LanguageBase):
    db.query(models.Language).filter(models.Language.id == lang_id).update(lang.dict())
    db.commit()
    return db.query(models.Language).filter(models.Language.id == lang_id).first()
