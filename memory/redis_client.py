import os
import redis
from dotenv import load_dotenv
import json

load_dotenv()

redis_url = os.getenv("REDIS_URL")

redis_client = redis.Redis.from_url(redis_url, decode_responses=True)

def save_to_redis(session_id: str, key: str, value: dict):
    """Stores a namespaced key with serialized JSON value."""
    namespaced_key = f"{session_id}:{key}"
    redis_client.set(namespaced_key, json.dumps(value))

def get_from_redis(session_id: str, key: str) -> dict | None:
    """Gets the deserialized JSON value."""
    namespaced_key = f"{session_id}:{key}"
    raw = redis_client.get(namespaced_key)
    return json.loads(raw) if raw else None

def delete_session_memory(session_id: str):
    """Optionally remove all keys under a session prefix (if you use HSET later)."""
    for key in redis_client.scan_iter(f"{session_id}:*"):
        redis_client.delete(key)

# For debugging
if __name__ == "__main__":
    sid = "demo-session"
    print(get_from_redis(sid, "news"))
    print(get_from_redis(sid, "signal"))
    print(get_from_redis(sid, "decision"))
