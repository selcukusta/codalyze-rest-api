from pydantic import BaseModel
import typing as t

Threshold = t.NewType("Threshold", t.Mapping)


class Request(BaseModel):
    html: str
    threshold: Threshold
