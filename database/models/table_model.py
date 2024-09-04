from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import BigInteger


class Base(DeclarativeBase):
    pass


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class UsersModel(AbstractModel):
    user_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    height: Mapped[float] = mapped_column()
    date: Mapped[float] = mapped_column()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, user_id={self.user_id!r}, name={self.name!r}, age={self.age!r}, height={self.height!r}, date={self.date!r})"
