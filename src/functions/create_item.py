import json
from utils.db import get_connection

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))

        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO items (name, description) VALUES (%s, %s)",
                (body['name'], body['description'])
            )
            connection.commit()

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Item created successfully"})
        }

    except Exception as e:
        print(f"Error occurred: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal server error",
                "error": str(e)  # Include actual error in response for debugging (remove in prod)
            })
        }
