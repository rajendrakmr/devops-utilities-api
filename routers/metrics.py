from fastapi import APIRouter,HTTPException
from services.metrics_services import get_system_metrics
router = APIRouter()

@router.get('/metrics',status_code=200)
def get_metrics():
    """
    This is metrics API return the system usage percent
    """
    try:
        metrics= get_system_metrics()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail ="Server error"
        )


