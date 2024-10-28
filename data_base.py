from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession


from App.config import DATA_BASE_URL
from sqlalchemy.orm import sessionmaker


async_engine =AsyncEngine(
    create_engine(
        url=DATA_BASE_URL,
        echo=True
    )
)

async def init_db():
    async with async_engine.begin() as conn:
        from App.db.models import User

        await conn.runs_sync(SQLModel.metadata.create_all())


async def get_session()->AsyncSession:

    Session =sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
