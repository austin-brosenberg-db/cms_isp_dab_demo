from pyspark.sql import SparkSession, DataFrame
import os

def get_taxis(spark: SparkSession) -> DataFrame:
  return spark.read.table("samples.nyctaxi.trips")


# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html.
def get_spark() -> SparkSession:
# try:
  # from databricks.connect import DatabricksSession
  # spark = DatabricksSession.builder.remote(
  #   host       = f"https://e2-demo-field-eng.cloud.databricks.com/",
  #   token      = os.environ['DATABRICKS_PAT'],
  #   cluster_id = "0730-180525-bdpqfev2"
  # ).getOrCreate()
  from databricks.connect import DatabricksSession
  from databricks.sdk.core import Config

  pat = os.environ['DATABRICKS_PAT']
  print("this is the pat " + pat)
  print("this is a test " + os.environ['TEST'])

  config = Config(
    host       = f"https://e2-demo-field-eng.cloud.databricks.com/",
    token      = pat,
    cluster_id = "0917-140040-lfy5g5bz"
  )
  return DatabricksSession.builder.sdkConfig(config).getOrCreate()
# except ImportError:
#   return SparkSession.builder.getOrCreate()

def main():
  get_taxis(get_spark()).show(5)

if __name__ == '__main__':
  main()
