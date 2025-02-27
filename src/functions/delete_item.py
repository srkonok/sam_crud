import json
from utils.db import get_connection

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']

        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
            connection.commit()

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Item deleted successfully"})
        }

    except Exception as e:
        print(f"Error occurred: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal server error",
                "error": str(e)  # Include actual error for debugging (remove in prod for security)
            })
        }
