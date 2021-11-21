from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text,ForeignKey,Date
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__='t_akun'
    id_anggota=Column(Integer, primary_key=True, autoincrement=True,nullable=False,unique=True)
    email=Column(String(255),nullable=False,unique=True)
    username=Column(String(255),nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    nama=Column(String(255),nullable=False,unique=True)
    departemen=Column(String(255), nullable=False)
    ttl=Column(Date, nullable=False)
    no_telp=Column(String(15), nullable=False)
    role=Column(String(50), nullable=False)
    relation_tugas = relationship("Tugas")
    

    # def __repr__(self):
    #      return f"<Item name={self.name} price={self.price}>"

class Kegiatan(Base):
    __tablename__='t_kegiatan'
    id_kegiatan=Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nama_kegiatan=Column(String(255),nullable=False,unique=True)
    # list_tugas=Column("Tugas", back_populates="nama_kegiatan", nullable=True)
    start_kegiatan = Column(Date, nullable=False)
    end_kegiatan = Column(Date, nullable=False)
    relation_tugas = relationship("Tugas")

class Tugas(Base):
    __tablename__='t_tugas'
    id_tugas=Column(Integer,primary_key=True, autoincrement=True, unique=True)
    nama_tugas=Column(String(255),nullable=False, unique=True)
    id_anggota=Column(Integer)
    nama=Column(String(255),ForeignKey('t_akun.nama'))
    departemen=Column(String(255))
    id_kegiatan=Column(Integer)
    nama_kegiatan=Column(String(255),ForeignKey('t_kegiatan.nama_kegiatan'))
    description=Column(String(255), nullable=False)
    tanggal_pemberian = Column(Date)
    tenggat_waktu = Column(Date)
    status=Column(String(50), nullable=False, default="Assigned")
    hasil_tugas=Column(String(255),nullable=True, default="No Submission")
    relation_penilaian = relationship("Penilaian")
    

class Penilaian(Base):
    __tablename__='t_penilaian'
    id_tugas=Column(Integer, primary_key=True)
    nama_tugas=Column(String(255),ForeignKey('t_tugas.nama_tugas'), nullable=False)
    id_kegiatan=Column(Integer)
    nama_kegiatan=Column(String(255))
    id_anggota=Column(Integer)
    nama=Column(String(255))
    departemen=Column(String(255))
    hasil_tugas=Column(String(255), nullable=True, default="No Submission")
    nilai=Column(Integer, nullable=True, default=0)
    komentar=Column(String(255), nullable=True, default="No comment")  
