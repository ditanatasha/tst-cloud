from os import stat
from datetime import date, datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud, models, schemas


app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")  # define path operation decorator.
async def root(): # Python function. The use of async is optional.
    return {"Hello": "RPL"}

#Kegiatan

#View semua kegiatan yang ada
@app.get('/kegiatan_all',response_model=List[schemas.Kegiatan], status_code=200)
def get_all_kegiatan(db: Session = Depends(get_db)):
    kegiatan=db.query(models.Kegiatan).all()

    return kegiatan

#View kegiatan berdasarkan id nya
@app.get('/kegiatan',response_model=schemas.Kegiatan, status_code=200)
def get_one_kegiatan(id_kegiatan:int, db: Session = Depends(get_db)):
    db_kegiatan=db.query(models.Kegiatan).filter(models.Kegiatan.id_kegiatan == id_kegiatan).first()
    if db_kegiatan is None:
        raise HTTPException(status_code=400, detail="Kegiatan not found")
    return db_kegiatan

#Create kegiatan baru
@app.post('/kegiatan',response_model=schemas.Kegiatan)
def create_kegiatan(nama_kegiatan:str, start_kegiatan: date, end_kegiatan: date, db: Session = Depends(get_db)): 
    check_db_kegiatan = db.query(models.Kegiatan).filter(models.Kegiatan.nama_kegiatan==nama_kegiatan).first()
    if check_db_kegiatan is not None:
        raise HTTPException(status_code=400, detail="Kegiatan already registered")
    db_kegiatan = crud.create_kegiatan(nama_kegiatan, start_kegiatan, end_kegiatan, db)
    return (db_kegiatan)
    raise HTTPException(
        status_code=404, detail=f"Kegiatan addition failed."
    )

#Update detail kegiatan
@app.put('/kegiatan',response_model=schemas.Kegiatan )
def update_kegiatan(id_kegiatan:str, new_nama_kegiatan:str, new_start_kegiatan: date, new_end_kegiatan: date, db: Session = Depends(get_db)):
    update_db_kegiatan = db.query(models.Kegiatan).filter(models.Kegiatan.id_kegiatan==id_kegiatan).first()
    if update_db_kegiatan is None:
        raise HTTPException(status_code=400, detail="No Kegiatan registered")
    update_db_kegiatan.nama_kegiatan=new_nama_kegiatan
    update_db_kegiatan.start_kegiatan=new_start_kegiatan
    update_db_kegiatan.end_kegiatan=new_end_kegiatan

    db.commit()

    return update_db_kegiatan
    raise HTTPException(
        status_code=404, detail=f'Kegiatan failed to update.'
      )

#Menghapus kegiatan
@app.delete('/kegiatan', response_model=List[schemas.Kegiatan] )
def delete_kegiatan(id_kegiatan:int, db: Session = Depends(get_db)):
    delete_kegiatan=db.query(models.Kegiatan).filter(models.Kegiatan.id_kegiatan==id_kegiatan).all()
    if delete_kegiatan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Kegiatan Not Found")
       
    db.delete(delete_kegiatan)
    db.commit()

    return delete_kegiatan
    raise HTTPException(
        status_code=404, detail=f'Kegiatan failed to delete.'
      )

