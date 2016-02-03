from pyspark import SparkContext

sc = SparkContext(master='local[*]', appName='MyPySparkScript')
rdd = sc.parallelize([1,2,3,4,5])
print(rdd.count())
