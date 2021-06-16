from faker import Faker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
fake = Faker()

for _ in range(100):
    Path(BASE_DIR / fake.file_name()).touch()
    