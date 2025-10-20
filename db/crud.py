from sqlalchemy import select
from db.models import Users, Messages
from db.db_session import async_session_maker

async def get_user(id_tg: str):
    async with async_session_maker() as session:
        result = await session.execute(
            select(Users).filter_by(id_tg=id_tg)
        )
        return result.scalar_one_or_none()

async def create_user(id_tg: str):
    async with async_session_maker() as session:
        user = Users(id_tg=id_tg)
        session.add(user)
        await session.commit()
        return user

async def create_message(id_user: int, message_id: int, message_text: str):
    async with async_session_maker() as session:
        message = Messages(
            id_user=id_user,
            id_tg_message=message_id,
            text_message=message_text
        )
        session.add(message)
        await session.commit()
        return message