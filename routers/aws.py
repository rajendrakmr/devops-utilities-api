from fastapi import APIRouter,HTTPException
from services.s3_service import get_s3_buckets
router = APIRouter()

@router.get('/s3',status_code=200)
def get_buckets():
    """
   This API get the buckets list as per the date time creation new old as per the last 90 days.
    """
    try:
        buckets= get_s3_buckets()
        return buckets
    except:
        raise HTTPException(
            status_code=500,
            detail ="Server error"
        )


