## Scenario 3
For the third chapter/sprint, you need to create an orchestrated pipeline that will allow all stages to run in a managed way. The pipeline should run daily and make data available at 10:00 AM EET. It should extract data into the bronze layer (raw zone) named *lead_raw*, apply necessary transformations into the silver layer (staging zone) named *lead_staging*, and upload data to the golden layer (trusted zone) named *lead_trusted* for consumption in the analytical process. It is required that the golden layer contains four tables: a financial table for payment calculations, a technical table for analyzing technical issues, a non-PII table for access by all users with limited access levels across the organization, and a PII table for users with high access levels.

## Instructions 3
Use the directory `chapter_3/work_3/` as your project directory for work related to **Chapter 3** for **LeadData** company.

## Assignment 3
a. Setup Docker container:
* i. Run Docker Desktop.
Used Podman instead of Docker Desktop
* ii. Retrieve Docker Compose file.
Used the docker-compose file in podman
* iii. Update Docker Compose file.
Updated the Docker Compose file
* iv. Add requirements.
Added neccesary reqs for the project ------  "dbt-core==1.8.0  dbt-postgres==1.8.2 faker==18.4.0 polars==1.8.1"
* v. Create Dockerfile.
Used  ------   "podman compose --file .\docker-compose.yml up"

b. Create dbt:
* i. Create project.
* ii. Create profiles.
* iii. Create sources.
* iv. Create models.

dbt up and running


c. Create Airflow:
* i. Run containers.
* ii. Login.
* iii. Setup Connection.
* iv. Create DAG.
* v. Run DAG.
Found a problem where there were multiple lines with Headers that resulted in a fail state in Airflow.
"""
psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type numeric: "personal_number"
CONTEXT:  COPY raw_batch_data, line 1108, column personal_number: "personal_number"

"""
Solved it by checking if the file exists, if it existed then i would not add another header row in from lines 93 -> 98
Containers created, could login on localhost:8080 and see the created DAG. Runned it with a status of succes in 23 seconds

d. Setup pgAdmin 4 database:
* i. Connect to database.
Connected to the airflow from pgAdmin 4
* ii. Check data in database.
Data uploaded and ok