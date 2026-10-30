from pyspark.sql import SparkSession
import os


def test_pytest_works():
    pass


def test_package_is_importable():
    import orders_pipeline


def test_spark_is_available():
    spark = SparkSession.builder.getOrCreate()
    assert spark.range(5).count() == 5


def test_catalog_schemas_exist():
    spark = SparkSession.builder.getOrCreate()
    schemas = spark.sql("SHOW SCHEMAS IN retail_dev").collect()
    schema_names = [row.databaseName for row in schemas]
    expected = {"bronze", "silver", "gold"}
    missing = expected - set(schema_names)
    assert not missing, f"Missing schemas in retail_dev: {missing}"


def test_raw_volume_is_accessible():
    path = "/Volumes/retail_dev/bronze/raw"
    assert os.path.isdir(path), f"Volume not found: {path}"
