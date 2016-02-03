# Python and Spark for Data Analysis

These are the IPython notebooks I used for a 4-day training course on Python and Spark for data science, given in December 2015 to a [Data Minded](http://www.dataminded.be) client.  The audience consisted of experienced data analysts, familiar with technologies like `R` and `SPSS`, but who had never used Python and had never worked on a Hadoop cluster.

The content is mildly redacted to remove all references to the actual client, but are otherwise unchanged.

Each day consisted of working through a series of IPython notebooks.  Exercises are interspersed throughout.  The last notebook of each day contains solutions to that day's exercises.

## Objectives

The objectives of the training were to:
* Learn the fundamentals of Python
* Learn the fundamentals of its statistical and machine learning packages
* Learn Apache Spark using Python
* Learn how to apply these technologies in a live Hadoop cluster

## Pre-requisites

Before the start of the course, we required the following software to be installed on students' laptops:
* [Anaconda 2.4.1 64-bit for Windows](https://www.continuum.io/downloads#_windows).  The packages in this version of Anaconda [included](http://docs.continuum.io/anaconda/pkg-docs):
  - Python 2.7.11
  - IPython 4.0.1
  - NumPy 1.9.3
  - SciPy 0.16.0
  - Matplotlib 1.5.0
  - Pandas 0.17.1
  - Seaborn 0.6.0
  - Scikit-learn 0.17
* [Apache Spark 1.2.0](http://spark.apache.org/downloads.html).  The version was chosen to match that in the client's production cluster, even though the latest version at the time of the course was 1.5.2
* [JDK 7u79](http://www.oracle.com/technetwork/es/java/javase/downloads/jdk7-downloads-1880260.html).

## Syllabus

The four days covered the following content.

### Day 0: Fundamentals of Python

This day was intended for people with very limited programming experience and/or no Python experience. Day 0 was optional.

At the end of this day, the students were able to:
* Start and run python programs interactively with python CLI
* Use an IDE to write programs and execute them, including command line arguments
* Create notebooks locally and on a server
* Import libraries
* Store data in variables and understand their reach
* Know the standard operators
* Control the flow of a program
* Perform common string operations such as concatenation, substring, replace
* Use the correct data structures
* Use functions to structure your program

### Day 1: Statistical and Machine Learning Packages

On Day 1, we discussed several of the powerful statistical and machine learning libraries in Python.  It was purposely a very hands on introduction and we did not dive into the mathematics behind any of the algorithms.

At the end of this day, the students were able to:
* Import and export data in csv
* Use numpy/scipy to perform mathematical computations
* Slice and dice data
* Use pandas to wrangle data
* Plot data and perform exploratory analysis
* Use `scikit-learn`
* Perform regression analysis in Python
* Perform classification analysis in Python

### Day 2: Apache Spark and Python

On the second day, we dove into Spark. We focused on the essential parts. After a brief introduction into Spark Core, we explored Spark SQL and Spark MLlib.

At the end of this day, the students were able to:
* Understand the role of Spark and pyspark in the eco-system
* Run spark locally from a shell
* Run spark locally in IPython Notebooks
* Do a word count on an input file
* Load data in SparkSQL
* Query data in SparkSQL
* Use Spark MLlib to perform regression and classification analyses at scale

### Day 3: Python and Apache Spark on a Cluster

In this last day, we set up a small Cloudera Hadoop cluster on AWS and explored how everything we had learned could be run in a cluster environment.  The second half of the day was set aside for an open-ended project.  Possible projects included:
1. setting up a machine learning pipeline on data from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/);
2. implementing a machine learning algorithm using Spark Core;
3. testing to what extent Spark running times scales linearly with data size.

At the end of this day, the students were able to
* Run python scripts on the cluster from a shell and from ipython notebooks
* Use Spark to read from and write to HDFS
* Use SparkSQL to read data from and write data to Hive
* Understand how YARN works
* Submit spark jobs on the cluster
* Use Spark, SparkSQL and Spark MLlib to run algorithms on large-scale data.