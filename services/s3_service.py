
import boto3
from datetime import datetime, timedelta,timezone

def get_s3_buckets():
    """
        This API get the buckets list as per the date time creation new old as per the last 90 days.
    """
    try:
        client = boto3.client('s3')
        # print(client)
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

    except Exception as e:
        print("Error list bucket:", e)
        