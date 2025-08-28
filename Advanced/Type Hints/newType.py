from typing import NewType

# Create new types
UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

# Define functions that use the new types
def get_user_name(user_id: UserId) -> str:
   return f"User with ID {user_id}"

def get_product_name(product_id: ProductId) -> str:
   return f"Product with ID {product_id}"

# Example usage
user_id = UserId(42)
product_id = ProductId(101)

print(get_user_name(user_id))   # Output: User with ID 42
print(get_product_name(product_id))  # Output: Product with ID 101