from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum as spark_sum

# Inicializar SparkSession
spark = SparkSession.builder \
    .appName("E-Commerce Orders Analysis") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Ruta del CSV montado en el contenedor
input_path = "/opt/spark/input/e-commerce_orders.csv"

# Leer CSV
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Mostrar esquema y primeras filas
print("Esquema del DataFrame:")
df.printSchema()
print("Primeras filas:")
df.show(5)

# Ejemplo de análisis: total de órdenes por cliente
orders_per_customer = df.groupBy("customer_id").agg(
    count("*").alias("total_orders"),
    spark_sum(col("order_value")).alias("total_spent")
).orderBy(col("total_spent").desc())

# Mostrar resultados
print("Top 10 clientes por gasto total:")
orders_per_customer.show(10)

# Guardar resultados en carpeta spark-data (persistente)
output_path = "/opt/spark/data/orders_summary"
orders_per_customer.coalesce(1).write.mode("overwrite").csv(output_path, header=True)

# Finalizar Spark
spark.stop()
