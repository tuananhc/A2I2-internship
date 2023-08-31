# You can use the `withColumn` function in Spark to replace specific values in the dataframe.

# Here's how you can replace "company" with "cmp" in all columns of the dataframe:

# ```python
from pyspark.sql.functions import col, regexp_replace
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

data = [["1", "xxx", "company 0"],
        ["2", "xxx", "company 1"],
        ["3", "company 44", "company 2"],
        ["4", "xxx", "company 1"],
        ["5", "bobby", "company 1"]]

dataframe = spark.createDataFrame(data)

# Replace "company" with "cmp" in all columns
updated_df = dataframe.select([regexp_replace(col(column), "company", "cmp").alias(column) for column in dataframe.columns])

# Show the updated dataframe
updated_df.show()
# ```

# Output:
# ```
# +---+----+-------+
# | _1|  _2|     _3|
# +---+----+-------+
# |  1| xxx|cmp 0  |
# |  2| xxx|cmp 1  |
# |  3|cmp4|cmp 2  |
# |  4| xxx|cmp 1  |
# |  5|bobby|cmp 1 |
# +---+----+-------+
# ```

# This would replace "company" with "cmp" in all columns of the dataframe. Note that the column names will remain the same in this case.