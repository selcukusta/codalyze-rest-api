from pydantic import BaseModel


class Threshold(BaseModel):
    cyclomatic_complexity: int
    lines_of_code: int
    parameter_count: int
