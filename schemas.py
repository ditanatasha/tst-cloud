from typing import List, Optional
from datetime import date
from pydantic import BaseModel

class User(BaseModel): #serializer
    id_anggota:int
    email:str
    username:str
    password:str
    nama:str
    departemen: str
    ttl:date
    no_telp:str
    role:str

    class Config:
        orm_mode=True

class Kegiatan(BaseModel): #serializer
    id_kegiatan: int
    nama_kegiatan: str
    start_kegiatan: date
    end_kegiatan: date
    
    class Config:
        orm_mode=True
    
class CreateKegiatan(BaseModel):
    nama_kegiatan: str
    start_kegiatan: date
    end_kegiatan: date

class Tugas(BaseModel): #serializer
    id_tugas: int
    nama_tugas: str
    id_anggota: int
    nama: str
    departemen: str
    id_kegiatan: str
    nama_kegiatan:str
    tanggal_pemberian: date
    tenggat_waktu: date
    status: str
    hasil_tugas: str
    description: str

    class Config:
        orm_mode=True

class CreateTugas(Tugas):
    nama_tugas: str
    nama: str
    nama_kegiatan: str
    tanggal_pemberian: date
    tenggat_waktu: date
    description: str

class Penilaian(BaseModel):
    id_kegiatan:int
    nama_kegiatan:str
    id_tugas: int
    nama_tugas:str
    id_anggota: int
    nama: str
    departemen: str
    hasil_tugas: str
    nilai: int
    komentar: str

    class Config:
        orm_mode=True
