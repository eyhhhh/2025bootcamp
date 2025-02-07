import aioredis

REDIS_URL = "redis://127.0.0.0:6379"
async def get_redis():
  return await aioredis.from_url(REDIS_URL, decode_response=True)