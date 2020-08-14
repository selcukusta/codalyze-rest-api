# -*- coding: utf-8 -*-

"""
This module extends the default output formatting to include HTML.
"""

import sys
import datetime
from jinja2 import Template


def html_output(source, header, thresholds):
    source_file_dict = {"filename": source.filename}
    func_list = []
    for source_function in source.function_list:
        if source_function:
            source_function_dict = source_function.__dict__
            func_list.append(source_function_dict)
            source_file_dict["functions"] = func_list

    with open("./assets/report.html") as f:
        output = Template(f.read()).render(
            header=header,
            date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            thresholds=thresholds,
            argument=source_file_dict,
        )
        return output
