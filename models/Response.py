class Response(object):
    def __init__(self, total_lines_of_code: int, function_list: list):
        self.total_lines_of_code = total_lines_of_code
        self.functions = [item.serialize() for item in function_list]

    def serialize(self):
        return {
            "total_lines_of_code": self.total_lines_of_code,
            "functions": self.functions,
        }
