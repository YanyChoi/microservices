import asyncio
import aiomysql
from app.core.config import settings

async def get_connection():
    return await aiomysql.connect(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        db=settings.MYSQL_DB,
        autocommit=False
    )

async def get_cursor():
    async with get_connection() as conn:
        return await conn.cursor()
    
loop = asyncio.get_event_loop()