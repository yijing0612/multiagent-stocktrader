from sqlalchemy import text
from memory.postgres import engine  # Your existing SQLAlchemy engine

with engine.connect() as conn:
    conn.execute(text("""
        ALTER TABLE trade_memory 
        ADD COLUMN IF NOT EXISTS trade_outcome TEXT DEFAULT 'Pending';
    """))
    conn.commit()