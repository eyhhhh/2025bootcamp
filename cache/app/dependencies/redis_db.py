from redis import asyncio as aioredis

# db와 연결
REDIS_URL = "redis://127.0.0.1:6379"
async def get_redis():
  return await aioredis.from_url(REDIS_URL, decode_responses=True)