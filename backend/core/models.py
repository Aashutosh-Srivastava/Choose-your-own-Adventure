from typing import List, Optional,Dict,Any
from pydantic import BaseModel, Field


class StoryOptional(BaseModel):
    text:str=Field(description="The text of the option shown to user")
    nextNode:Dict[str,Any]=Field(description="The next node content and its option")

    