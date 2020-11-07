# SparkStreamingPipeline
This Data pipeline read the data from `Stream_input_location` which is landing path as CSV files arrived in landing path and apply user defined schema which defined in config.ini .
and print the output of input files data into batch as soon as input csv files arrived into `Stream_input_location` directory.

Note :in this project, i have defined all paths and schema in separate configuration file(config.ini) and used in main pipeline using configparser

Sample output of data on console


20/11/07 16:47:39 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
-------------------------------------------
Batch: 0
-------------------------------------------
| +---+----+---+ |
|----------------|
| | id|name|age| |
| +---+----+---+ |
| |  1| raj| 19| |
| |  2| sid| 20| |
| |  3| dev| 21| |
| |  4|navi| 19| |
| |  5| jai| 20| |
| |  6|veer| 21| |
| |  7| raj| 22| |
| +---+----+---+ |

-------------------------------------------
Batch: 1
-------------------------------------------
| +---+----+---+ |
|----------------|
| | id|name|age| |
| +---+----+---+ |
| |  5| jai| 20| |
| |  6|veer| 21| |
| |  7| raj| 22| |
| +---+----+---+ |

-------------------------------------------
Batch: 2
-------------------------------------------
| +---+----+---+ |
|----------------|
| | id|name|age| |
| +---+----+---+ |
| |  2| sid| 20| |
| |  3| dev| 21| |
| |  4|navi| 19| |
| +---+----+---+ |

Note : more SparkStreaming related operations will be added to this project and will publish 