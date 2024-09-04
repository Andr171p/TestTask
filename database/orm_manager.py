from typing import List, Sequence

from sqlalchemy import select

from database.db import db_manager, get_session, DatabaseSessionManager
from database.models.table_model import AbstractModel, UsersModel

from misc.utils import str_to_timestamp


class ORMManager(DatabaseSessionManager):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(UsersModel.metadata.drop_all)
            await connection.run_sync(UsersModel.metadata.create_all)

    async def create_user(
            self, user_id, name: str, age: int, height: float, date: str
    ) -> UsersModel:
        date = str_to_timestamp(date=date)
        async with self.session() as session:
            user = UsersModel(
                user_id=user_id,
                name=name,
                age=age,
                height=height,
                date=date
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def get_user(self, user_id) -> UsersModel:
        async with self.session() as session:
            user = await session.execute(
                select(UsersModel).where(UsersModel.user_id == user_id)
            )
            return user.scalars().one()

    async def get_users(self) -> Sequence[UsersModel]:
        async with self.session() as session:
            users = await session.execute(
                select(UsersModel)
            )
            return users.scalars().all()

    async def clear_table(self):
        async with self.connect() as connection:
            await connection.run_sync(UsersModel.metadata.drop_all)
            await connection.run_sync(UsersModel.metadata.create_all)


orm_manager = ORMManager()


'''import asyncio
from faker import Faker
import random
# orm_manager = ORMManager()
faker = Faker()
heights = [1.75, 2.01, 1.64, 1.55, 1.87]
count_of_fake_data = 5
for i in range(count_of_fake_data):
    user_id = faker.random_int(min=1000, max=9999)
    name = faker.first_name()
    age = faker.random_int(min=18, max=99)
    height = random.choice(heights)
    date = str(faker.date_time_this_century())
    asyncio.run(orm_manager.create_user(
        user_id=user_id,
        name=name,
        age=age,
        height=height,
        date=date
    ))'''

'''import asyncio


print(asyncio.run(orm_manager.get_users()))'''