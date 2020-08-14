from pydantic import BaseModel
from . import Threshold as t


class Request(BaseModel):
    html: str
    threshold: t.Threshold
