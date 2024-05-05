import aioredis

redis = aioredis.from_url("redis://localhost:6579",
                          encoding="utf-8", decode_response=True)
