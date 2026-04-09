from pydantic import BaseModel
from typing import Optional

class Action(BaseModel):
    action_type: str
    content: str

class Observation(BaseModel):
    email_text: str
    expected_label: Optional[str] = None
    agent_output: Optional[str] = None

class Reward(BaseModel):
    value: float
