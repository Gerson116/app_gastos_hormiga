
class TableConfig:
    TABLES = [
        {
            "name": "bills",
            "partition_key": "BillId",
            "description": "Table to store bills"
        },
        {
            "name": "categories",
            "partition_key": "CategoryId",
            "description": "Table to store categories"
        },
        {
            "name": "users",
            "partition_key": "UserId",
            "description": "Table to store users"
        }
    ]