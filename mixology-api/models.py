from uuid import UUID, uuid4
from enum import StrEnum, auto

from sqlalchemy import Uuid, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Alcohol(StrEnum):
    VODKA = auto()
    WHISKEY = auto()
    RUM = auto()
    GIN = auto()
    TEQUILA = auto()
    BRANDY = auto()
    LIQUEUR = auto()

class Drink(Base):
    __tablename__ = "drinkEntity"

    id: Mapped[Uuid] = mapped_column(primary_key=True, defaul=uuid4)
    base_drink: Mapped[list[Alcohol]] = mapped_column()
    name: Mapped[str] = mapped_column()
    component_ids: Mapped[list[UUID]] = mapped_column(ForeignKey("componentEntity.id"))
    drinks: Mapped["Component"] = relationship(back_populates="components")
    
class Component(Base):
    __tablename__ = "componentEntity"

    id: Mapped[Uuid] = mapped_column(primary_key=True, defaul=uuid4)
    components: Mapped["Drink"] = relationship(back_populates="drinks")
