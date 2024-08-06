from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


from app.core import config

DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=config.DEBUG, future=True)


async_session = async_sessionmaker(engine, class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session