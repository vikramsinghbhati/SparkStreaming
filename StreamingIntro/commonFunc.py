from pyspark.sql.types import StringType,IntegerType,StructType,StructField

def read_schema(schema_arg):
    mydict={
            "StringType()" : StringType(),
            "IntegerType()" : IntegerType()
            }

    split_val=schema_arg.split(",")
    schema=StructType()
    for i in split_val:
        x=i.split(" ")
        schema.add(x[0],mydict[x[1]],True)
    return schema

