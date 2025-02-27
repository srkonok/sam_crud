import json
from utils.db import get_connection

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        body = json.loads(event.get('body', '{}'))

        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE items SET name=%s, description=%s WHERE id=%s",
                (body['name'], body['description'], item_id)
            )
            connection.commit()

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Item updated successfully"})
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
