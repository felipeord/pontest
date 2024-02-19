"""Config async session for DE MYSQL"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.engine import URL

from app.config.settings import Settings, get_settings


class Engine:
    """Class for create engine"""

    def __init__(self, settings: Settings = get_settings()) -> None:
        self.url = URL.create(
            settings.DB_ENGINE,
            username=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_IP,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
        )
        self.engine = create_async_engine(
            self.url,
            pool_size=30,
            pool_timeout=30,
            pool_pre_ping=True,
            max_overflow=10,
            pool_recycle=1800,
        )
        self.session = async_sessionmaker(self.engine, expire_on_commit=False)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get session from engine"""
        async with self.session.begin() as session:
            yield session


engine = Engine()
