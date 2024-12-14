+-----------------------------------+
|        BaseInventoryItem          |
+-----------------------------------+
| name: str                         |
| quantity: int                     |
+-----------------------------------+
| + add_stock(amount: int): void    |
| + remove_stock(amount: int): void |
| + __str__(): str                  |
+-----------------------------------+

            ^
            |
+---------------------+         +----------------------+
|   RegularItem       |         |  PerishableItem      |
+---------------------+         +----------------------+
| + add_stock()       |         | expiry_date: str     |
| + remove_stock()    |         | + add_stock()        |
|                     |         | + remove_stock()     |
+---------------------+         +----------------------+

            ^
            |
+-----------------------+
|  InventorySection     |
+-----------------------+
| name: str             |
| items: dict           |
+-----------------------+
| + add_item()          |
| + remove_item()       |
| + get_item()          |
+-----------------------+

            ^
            |
+-----------------------+
|   InventoryManager    |
+-----------------------+
| sections: dict        |
+-----------------------+
| + add_section()       |
| + get_section()       |
| + add_stock()         |
| + remove_stock()      |
| + move_stock()        |
+-----------------------+

