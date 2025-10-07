from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from backend.app.database import Base


class Countries(Base):
    __tablename__ = "countries"

    index: Mapped[int] = mapped_column(Integer, primary_key=True)
    longitude: Mapped[float] = mapped_column(Float)
    latitude: Mapped[float] = mapped_column(Float)
    COUNTRY: Mapped[str] = mapped_column(String)
    ISO: Mapped[str] = mapped_column(String)


class Locations(Base):
    __tablename__ = "locations"

    index: Mapped[int] = mapped_column(Integer, primary_key=True)
    geonameID: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    ascii_name: Mapped[str] = mapped_column(String, key="asciiName")  # maps to asciiName in DB
    alternate_names: Mapped[str] = mapped_column(String, key="alternateNames")  # maps to alternateNames
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    country_code: Mapped[str] = mapped_column(String, key="country code")  # maps to 'country code'
    timezone: Mapped[str] = mapped_column(String)