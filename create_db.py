from database import Base,engine
from models import User, Kegiatan, Tugas, Penilaian

print("Creating database ....")

Base.metadata.create_all(engine)