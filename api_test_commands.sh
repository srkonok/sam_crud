# api_test_commands.sh

# Base URL (change if needed)
BASE_URL="https://abefxjojcg.execute-api.us-east-2.amazonaws.com/Prod"

# Create Item
curl -X POST "$BASE_URL/items" \
-H "Content-Type: application/json" \
-d '{"name": "Item 1", "description": "This is item 1"}'

# Read Item (Item ID: 1)
curl -X GET "$BASE_URL/items/1"

# Update Item (Item ID: 1)
curl -X PUT "$BASE_URL/items/1" \
-H "Content-Type: application/json" \
-d '{"name": "Updated Name", "description": "Updated description"}'

# Delete Item (Item ID: 1)
curl -X DELETE "$BASE_URL/items/1"
