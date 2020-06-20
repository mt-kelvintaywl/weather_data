# Components

## AWS Athena

[AWS Athena is a query service that scans and analyzes data in AWS S3.](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)

If you picture S3 as a medium for storing various data sources like a data lake, AWS Athena can be a very simple and powerful tool to perform ETL jobs.

AWS Athena provides a standard SQL interface to query your data sources.

Of course, you would thus need to define tables first.
In AWS Athena, these tables would be AWS Glue Tables.

## AWS Glue Table

An AWS Glue Table describes a schema over datasets on S3 or Kinesis data streams.
If you are already familiar with SQL, the interface to designing and creating one would feel similiar.

You can specify whether the table's dataset is in JSON, Arvo, CSV or Parquet format.

In particular, AWS Glue Table allows partitioning for efficient lookups and querying.
You may also notice that GCP's BigQuery also provides partitioning for similiar reasons.

One effective way to partition tables could be via the data record's ingestion or arrival time.
This allows efficient querying of events that happen within a specific window of time, for example.

Using AWS Glue jobs, you can also [query partitioned data](https://aws.amazon.com/blogs/big-data/work-with-partitioned-data-in-aws-glue/) through the provided AWS [DynamicFrame](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html)

## Kinesis Firehose

AWS Kinesis Firehose is a fully-managed delivery stream that empowers users to load data into designated data lakes like S3, or Redshift for instance.

It provides various features that allows you to transform your data before it reaches the destination too.

For instance, you can have [a Data Transformation Lambda that maps incoming CSV data into JSON](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html).

In addition, you can also [simply hook up format conversions to Parquet or ORC format through an AWS Glue Table definition.](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html)
