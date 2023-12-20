from redis import Redis
from dotenv import load_dotenv
import os
load_dotenv()
redis_host = os.getenv('CACHE_REDIS_HOST')
CACHE_REDIS_PORT= os.getenv('CACHE_REDIS_PORT')
CACHE_REDIS_PASSWORD= os.getenv('CACHE_REDIS_PASSWORD')
print(redis_host)
print(CACHE_REDIS_PORT)
print(CACHE_REDIS_PASSWORD)
import redis

r = redis.Redis(
  host=redis_host,
  port=CACHE_REDIS_PORT,
  password=CACHE_REDIS_PASSWORD)

r.ping() 

import redis



print('connected to redis "{}"'.format(redis_host)) 

