from fastapi import APIRouter,HTTPException 
from datetime import datetime
import psutil

router = APIRouter(tags=["System Probes"])

@router.get("/live")
def liveness_probe():
    """
    Liveness probe
    If this fails Kubernetes restarts the container

    """
    return {
        "status": "alive",
        "timestamp": datetime.utcnow()
    }



@router.get("/ready")
def readyness_probe():
    """
    Readyness probe
    If this fails Kubernetes stops sending traffic

    """

    cpu     = psutil.cpu_percent(interval=0.5)
    memory  = psutil.virtual_memory().percent

    return {
        "status": "ready",
        "cpu": cpu,
        "memory": memory
    }


@router.get("/startup")
def startup_probe():
    """
    Startup probe
    Used to verify application initialization
    """
    return {
        "status": "started"
    }