
class TableName:
    BILLS = 'bills'
    CATEGORIES = 'categories'
    USERS = 'users'

class TableConfig:
    TABLES = [
        {
            "name": TableName.BILLS,
            "partition_key": "BillId",
            "description": "Table to store bills"
        },
        {
            "name": TableName.CATEGORIES,
            "partition_key": "CategoryId",
            "description": "Table to store categories"
        },
        {
            "name": TableName.USERS,
            "partition_key": "UserId",
            "description": "Table to store users"
        }
    ]