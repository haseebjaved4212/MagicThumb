from datetime import datetime, timezone
from typing import Optional, List
from uuid import uuid4

from sqlmodel import Field, Relationship, SQLModel

def _uuid() -> str:
    return str(uuid4())