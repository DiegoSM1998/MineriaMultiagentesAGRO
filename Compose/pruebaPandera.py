import pandas as pd
import pandera as pa
from pandera import Column, Check

fruits = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Aldi", "Walmart", "Walmart", "Aldi"],
        "price": [2, 1, 3, 4],
    }
)
print(fruits)

available_fruits = ["apple", "banana", "orange"]
nearby_stores = ["Aldi", "Walmart"]
try:
    schema = pa.DataFrameSchema(
        {
            "name": Column(str, Check.isin(available_fruits)),
            "store": Column(str, Check.isin(nearby_stores)),
            "price": Column(int, Check.less_than(4)),
        }
    )

    schema.validate(fruits)
except Exception as ex:
    print(ex)
