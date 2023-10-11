import redis
from app.core.config import settings

class ConnectionPool:
    pool: redis.ConnectionPool
    def __init__(self):
        pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
    
    def get_connection(self):
        return redis.Redis(connection_pool=self.pool)

redis_pool = ConnectionPool()
redis_connection = redis_pool.get_connection()
