from sqlalchemy.orm import Session
from datetime import date
import models, schemas


def create_kegiatan(nama_kegiatan:str, start_kegiatan: date, end_kegiatan: date, db: Session):
    
    db_kegiatan = models.Kegiatan(
        nama_kegiatan=nama_kegiatan,
        start_kegiatan=start_kegiatan,
        end_kegiatan=end_kegiatan
    )

    db.add(db_kegiatan)
    db.commit()
    db.refresh(db_kegiatan)

    return db_kegiatan

