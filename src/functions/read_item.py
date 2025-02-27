import json
from utils.db import get_connection
from datetime import datetime

def default_serializer(obj):
    """ Convert datetime objects to string for JSON serialization. """
    if isinstance(obj, datetime):
        return obj.isoformat()  # e.g., '2025-02-28T14:23:45'
    raise TypeError(f"Type {type(obj)} not serializable")

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']

        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
            result = cursor.fetchone()

        if not result:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Item not found"})
            }

        # Use custom serializer to handle datetime fields
        return {
            "statusCode": 200,
            "body": json.dumps(result, default=default_serializer)
        }

    except Exception as e:
        print(f"Error occurred: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal server error",
                "error": str(e)  # Consider removing this for production
            })
        }
