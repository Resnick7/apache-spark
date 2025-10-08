from pyspark.sql import SparkSession

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Test Spark Docker") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

print("✅ SparkSession creada con éxito!")

# Crear un DataFrame de prueba
data = [("Antonella", 1), ("Capadona", 2), ("Spark", 3)]
df = spark.createDataFrame(data, ["nombre", "valor"])

# Mostrar datos
df.show()

# Operaciones simples
df_2 = df.withColumn("valor_doble", df.valor * 2)
df_2.show()

# Finalizar sesión
spark.stop()
print("✅ Prueba completada correctamente.")
