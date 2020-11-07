# SparkStreamingPipeline
This Data pipeline read the data from `Stream_input_location` which is landing path as CSV files arrived in landing path and apply user defined schema which defined in config.ini .
and print the output of input files data into batch as soon as input csv files arrived into `Stream_input_location` directory.

Note 1 :In this project, I have defined all paths and schema in separate configuration file(config.ini) and used in main pipeline using configparser

Note 2 : More SparkStreaming related operations will be added to this project and will publish 
