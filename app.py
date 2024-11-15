# author: brando
# date: 11/14/24
#
# https://realpython.com/api-integration-in-python/#fastapi
# uvicorn app:app --reload --host 0.0.0.0
# https://www.uvicorn.org/

from fastapi import FastAPI
from pydantic import BaseModel, Field
import psutil

app = FastAPI()

def _find_next_id():
    return max(country.country_id for country in countries) + 1

class Country(BaseModel):
    country_id: int = Field(default_factory=_find_next_id, alias="id")
    name: str
    capital: str
    area: int

countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]

@app.get("/countries")
async def get_countries():
    return countries

@app.post("/countries", status_code=201)
async def add_country(country: Country):
    countries.append(country)
    return country

class Stat(BaseModel):
    cpu_percent: float
    ram_percent: float
    disk_space_total: int
    disk_space_used: int
    disk_space_free: int
    disk_space_percent: float

@app.get("/stat")
async def get_stat():
    return Stat(
        cpu_percent=psutil.cpu_percent(),
        ram_percent=psutil.virtual_memory().percent,
        disk_space_total=psutil.disk_usage('/').total,
        disk_space_used=psutil.disk_usage('/').used,
        disk_space_free=psutil.disk_usage('/').free,
        disk_space_percent=psutil.disk_usage('/').percent
    )

