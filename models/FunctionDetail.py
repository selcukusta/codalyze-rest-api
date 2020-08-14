class FunctionDetail(object):
    def __init__(
        self,
        name,
        cyclomatic_complexity,
        lines_of_code,
        start_line,
        end_line,
        parameter_count,
    ):
        self.name = name
        self.cyclomatic_complexity = cyclomatic_complexity
        self.lines_of_code = lines_of_code
        self.start_line = start_line
        self.end_line = end_line
        self.parameter_count = parameter_count

    def serialize(self):
        return {
            "name": self.name,
            "cyclomatic_complexity": self.cyclomatic_complexity,
            "lines_of_code": self.lines_of_code,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "parameter_count": self.parameter_count,
        }
