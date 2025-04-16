## Scenario 9
For the ninth chapter/sprint, it is required to process, on a daily basis, the data from the previous week stored in the data lake in the S3 bucket. The processing should involve filtering and aggregating the data, as well as adding additional columns based on existing ones. After the transformations, the processed data must be written back to the *LeadData* data lake.

## Instructions 9
Use the directory `chapter_9/work_9/` as your project directory for work related to **Chapter 9** for **LeadData** company.

## Assignment 9
a. Develop local pipeline:
* i. Intro Google Colab Notebook.
Created an Google Colab Notebook    
* ii. Initialize PySpark Session.
Initialized PySpark Session with the code provided in the course
* iii. Data Processing.
Proccesed the data according to the guide
* iv. Data Analysis.
Analyzed and also viewed the data
* v. Validate transformed data.

b. Develop cloud pipeline:
* i. Check raw data.
* ii. Create IAM role.
Knowledge from previous chapters
* iii. Create Glue job.
Knowledge from previous chapters
* iv. Run Glue job.
Watched how a Glue job should work, be setup and managed
* v. Validate transformed data.
Only read through the course, the docs and youtube videos out of bill payments on AWS