from pydantic import BaseModel
import typing as t

Threshold = t.NewType("Threshold", t.Any)


class Request(BaseModel):
    html: str
    threshold: Threshold
