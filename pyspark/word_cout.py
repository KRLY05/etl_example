import pyspark

sc = pyspark.SparkContext("local[*]")
data = sc.textFile("./biographies.list")
lines = data.filter(lambda line: line[0:2] == "BG" and len(line) > 4)
words = lines.flatMap(lambda line: line.split(" "))
counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

if __name__ == "__main__":
    counts.saveAsTextFile("./output")
