from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from decouple import config

engine: AsyncEngine = create_async_engine(f"postgresql+asyncpg://{config('POSTGRES_USERNAME')}:{config('POSTGRES_PASSWORD')}@{config('POSTGRES_HOST')}:{config('POSTGRES_PORT')}/{config('POSTGRES_DATABASE')}", echo=True)
Base = declarative_base()

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # schema=config("POSTGRES_SCHEMA")