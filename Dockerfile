# Imagen base oficial de apache/spark-docker para Spark 3.5.7
FROM openjdk:17-slim

# Variables de entorno
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Instalar dependencias básicas
RUN apt-get update && apt-get install -y curl python3 python3-pip bash && \
    rm -rf /var/lib/apt/lists/*

# Descargar Spark 3.5.7 precompilado con Hadoop 3.3 y Scala 2.12
RUN curl -L https://archive.apache.org/dist/spark/spark-3.5.7/spark-3.5.7-bin-hadoop3.tgz \
    | tar -xz -C /opt/ && mv /opt/spark-3.5.7-bin-hadoop3 $SPARK_HOME

# Copiar requirements.txt si necesitás librerías Python adicionales
# COPY requirements.txt /tmp/
# RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /opt/spark

# Por defecto, arrancar bash (podés sobreescribir con master/worker)
CMD ["bash"]

LABEL maintainer="Antonella Capadona antocapatona7@gmail.com"
LABEL version="1.0"
LABEL description="Imagen de Apache Spark 3.5.7 con Python 3"