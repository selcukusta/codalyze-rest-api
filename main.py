import logging
import lizard
import tempfile
import os
import uuid
from models import Request as rq, Response as rs, FunctionDetail as fd, Extension as e
from output_generator import Output as o

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.get("/")
async def main_handler():

    return {
        "Title": "Codalyze: Code Complexity Report",
        "Description": "Create code complexity (Cyclomatic complexity, Lines Of Code, Parameter Count, etc.) report for the activated code file.",
        "Support": "selcukusta(at)gmail(dot)com",
        "API Documentation": "https://codalyze-api.selcukusta.com/docs",
        "Credits": {
            "lizard": "https://github.com/terryyin/lizard",
            "fastapi": "https://github.com/tiangolo/fastapi",
        },
    }


@app.post("/analyze/{extension}")
async def analyze_handler(extension: e.Extension, code: rq.Request):
    analyze_result = lizard.analyze_file.analyze_source_code(
        f"temp.{extension}", code.html
    )
    functions = [
        fd.FunctionDetail(
            item.name,
            item.cyclomatic_complexity,
            item.nloc,
            item.start_line,
            item.end_line,
            item.parameter_count,
        )
        for item in analyze_result.function_list
    ]
    result = rs.Response(analyze_result.nloc, functions)
    return result.serialize()


@app.post("/output/{extension}", response_class=HTMLResponse)
async def output_handler(extension: e.Extension, body: rq.Request):
    tmp = tempfile.NamedTemporaryFile(
        delete=False, prefix="code-", suffix=f".{extension}"
    )
    try:
        tmp.write(str.encode(body.html, encoding="utf-8"))
        tmp.close()
        analyze_result = lizard.analyze_file(tmp.name)
        return o.html_output(
            analyze_result, f"{uuid.uuid1()}.{extension}", body.threshold
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=500, detail="Report file cannot be generated. Please try again!"
        )
    finally:
        os.unlink(tmp.name)
