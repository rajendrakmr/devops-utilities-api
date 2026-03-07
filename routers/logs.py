
from fastapi import APIRouter
from pydantic import BaseModel
from services.log_service import analyze_logs

router = APIRouter(
    prefix="/logs",
    tags=["Log Analysis"]
)


class LogRequest(BaseModel):
    logs: list[str]


@router.post("/analyze")
def analyze_log_data(request: LogRequest):

    result = analyze_logs(request.logs)

    return {"summary": result}