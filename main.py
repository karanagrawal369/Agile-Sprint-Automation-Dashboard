from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from agents.manager import AgentManager
from my_logging import AgentLogger

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

manager = AgentManager()

@app.get("/")
async def index():
    return FileResponse("templates/index.html")

@app.post("/run/sprint-cycle")
def run_sprint():
    res = manager.run_sprint_cycle()
    return JSONResponse({"status": "done", "result": res})

@app.post("/agents/qa/generate")
def run_qa(sprint_id: str = "s1"):
    res = manager.run_qa_generation(sprint_id)
    return JSONResponse({"status": "done", "result": res})

@app.post("/agents/triage/run")
def run_triage():
    res = manager.run_triage()
    return JSONResponse({"status": "done", "result": res})

@app.get("/status")
def status():
    trace = AgentLogger.get_trace()
    last = manager.get_last_session()
    return JSONResponse({"trace": trace, "last_session": last})
