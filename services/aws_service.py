from datetime import datetime,date, timedelta,timezone
import boto3

def get_aws_cost():

    client = boto3.client("ce")

    end = date.today()
    start = end - timedelta(days=90)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": str(start),
            "End": str(end)
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    return response

def get_s3_buckets(): 
    client = boto3.client('s3') 
    response = client.list_buckets()
    current_date_time = datetime.now(timezone.utc)
    new_buckets=[]
    all_buckets=[]
    old_buckets=[]
    days_ago_90 = current_date_time - timedelta(days=30)
    for bucket in response["Buckets"]: 
        all_buckets.append(bucket)
        print(days_ago_90,bucket['CreationDate'])
        if bucket['CreationDate']<days_ago_90:
            old_buckets.append(bucket)
        else:
            new_buckets.append(bucket)


    return {
        "total_buckets":len(all_buckets),
        "new_bucketes":len(new_buckets),
        "old_buckets":len(old_buckets),
        "new_bucket_names":new_buckets,
        "old_bucket_names":old_buckets, 
    }

     
        