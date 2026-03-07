from fastapi import APIRouter,HTTPException
from services.aws_service import get_s3_buckets,get_aws_cost
from fastapi import APIRouter,HTTPException  
 
router = APIRouter(
    prefix="/aws",
    tags=["Aws Services"]
)
@router.get("/cost")
def aws_cost():
    """
     This API will return unbilled cost aws services.
    """
    return get_aws_cost()

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


