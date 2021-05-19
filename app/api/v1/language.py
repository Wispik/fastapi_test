from fastapi import APIRouter, Depends, Body, Path, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import schemas
import utils.crud.language as lang_utils
from utils.depends import get_db


router = APIRouter()


@router.get('/', response_model=list[schemas.Language])
def get_languages(db: Session = Depends(get_db)):
    return lang_utils.get_languages(db)


@router.get('/{lang_id}', response_model=schemas.Language)
def get_language(lang_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    if lang := lang_utils.get_language(db, lang_id):
        return lang
    raise HTTPException(status_code=404)


@router.post('/', response_model=schemas.Language)
def create_language(language: schemas.LanguageBase = Body(...), db: Session = Depends(get_db)):
    return lang_utils.create_language(db, language)


@router.delete('/{lang_id}', response_model=schemas.Message)
def delete_language(lang_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    if lang_utils.delete_language(db, lang_id):
        return schemas.Message(
            status='ok',
            text=f'Language(id={lang_id}) - deleted!'
        )
    else:
        return JSONResponse(
            content=schemas.Message(
                status='error',
                text=f'Language(id={lang_id}) - not deleted!'
            ).dict(),
            status_code=400
        )


@router.put('/{lang_id}', response_model=schemas.Language)
def update_language(lang_id: int = Path(..., ge=1), language: schemas.LanguageBase = Body(...), db: Session = Depends(get_db)):
    if upd_lang := lang_utils.update_language(db, lang_id, language):
        return upd_lang
    else:
        return JSONResponse(
            content=schemas.Message(
                status='error',
                text=f'Language(id={lang_id}) - update_error!'
            ).dict(),
            status_code=400
        )
