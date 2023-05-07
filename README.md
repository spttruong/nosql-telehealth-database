# NoSQL Telehealth Database

## Overview

This is a crude implementation of a noSQL (MongoDB) database for a fictional telehealth application.

As such, the data generated is also fictional/mock data and will contain some inconsistencies.

The data stored on this application includes the following document types: 

* `patient` - contains patient demographic data
* `patient_chart` - contains patient electronic medical records (EMRs)
* `provider` - contains data on employed health providers
* `appointment` - contains telehealth appointment data

You will notice within the actual database, there are actually only 3 document collections: patients, providers, and appointments. This is because the `patient_chart` document is embedded within the `patient` document (more on that later).

The Python scripts within this repository generate sample documents in the form of JSON files using the [Faker](https://faker.readthedocs.io/en/master/) package. The JSON files are then imported into MongoDB Compass, which is connected to a MongoDB cloud instance.

## Data Model Design

This database utilizes a a combination of both **embedded** and **normalized** data models. 

For more information on both of of these models, you can refer to [MongoDB's documenation](https://www.mongodb.com/docs/) on [Data Model Design](https://www.mongodb.com/docs/manual/core/data-model-design/#embedded-data-models).

### Embedded Data Model

As the name suggests, in the embedded data model, documents "contain" other documents. That is to say, they have other documents embedded inside them. This model is particularly useful for one-to-one document relationships where a user querying a document would often query for another related document. The embedded model also supports many-to-one relationships where multiple documents can be embedded within a single document. However, this runs the risk of creating documents that are too large to manage.

### Normalized Data Model

In the normalized data model, documents contain **references**, usually in the form of an `id` field to refer to other documents. This is different from the embedded data model in the sense that different document types are kept in separate collections and are linked via the aforementioned reference field. This is similar to the concept of SQL foreign keys, which link entities in one table to another table in the database.

## Document Collections

There are 4 types of documents within the database:

1. `patient`
2. `patient_chart`
3. `provider`
4. `appointment`

### Document Relationship Diagram 

It may first be useful to visualize the document relationships similar to how we visualize entities in a relational database:

![image](https://user-images.githubusercontent.com/49035567/236642825-e28b7092-8600-4554-924f-85e706de47ce.png)

* Each `patient` has exactly one `patient_chart` that holds their medical data (one-to-one relationship) and vice versa. Each `patient_chart` holds the health data of exactly one `patient`.
* One `patient` may have a record of multiple `appointments` within their medical history (one-to-many relationship).
* Each `appointment` can be linked to one and only one `patient` as well as one and only one `provider`.
* One `provider` can conduct multiple `appointments` (one-to-many relationship).
* Multiple `appointments` can be linked to a single `patient_chart` (many-to-one relationship).

However, document relationships are a little different from relational database entity relationships as described in section, Data Model Design. Here is a more accurate way to view the document relationships:

![image](https://user-images.githubusercontent.com/49035567/236642813-e95fc80e-4172-4ac2-aa00-7c0ddcf6e41b.png)

* The `patient_chart` document is embedded within the `patient` document; in other words althought it is its own document, it is a part of the `patient` document
* The rest of the documents are related to one another via a referencing an `id` field

Here is the diagram with both relationships types overlayed for provide a more holistic view of the database:

![image](https://user-images.githubusercontent.com/49035567/236642758-63888b7d-0824-4a97-ae77-8f051dddf4ff.png)

These diagrams were created using [Lucid.app](lucid.app).

## Repository User Guide

From a user perspective, if you want to just extract the mock data to play around with it, navigate to `output/` and download `appointments.json`, `patients.json`, and `providers.json`.

If you want to test out the data generation, you can execute `make_mock_data.py` located at the root of the repository from the command line:

`$ python make_mock_data.py`

The resulting JSON files can be found in `output/`

----

The repository looks like this:

![image](https://user-images.githubusercontent.com/49035567/236650602-16d711ff-0dfc-4cc4-8208-ca8192c250a5.png)

There are three main folders within the repo.

* `document_generator/` contains the scripts that generate fake patient, provider, and appointment data respectively
  * Note: the scripts are currently set up to generate 50 records for each document type 
* `output/` contains the output JSON files (the files created from `make_mock_data.py`
* `sample_documents/`, which contains templates/rough drafts of what a each document should look like 

## Loading into MongoDB Compass

I am using a free MongoDB Atlas instance to store the data. I've also downloaded MongoDB Compass to manage and query the database. Therefore, the following steps will be demonstrated using the MongoDB Compass UI.

Click on the + icon to create a new database:

<img width="253" alt="image" src="https://user-images.githubusercontent.com/49035567/236650959-c71a6e78-ae2b-46db-b05a-b52376769f3f.png">

Name the database as well as the first collection within the database.

<img width="592" alt="image" src="https://user-images.githubusercontent.com/49035567/236651719-94854822-6a30-4523-bea9-eda6080fb303.png">

Proceed to create collections for the other document types as well.

<img width="256" alt="image" src="https://user-images.githubusercontent.com/49035567/236651753-05268306-317b-4ed7-bdbb-87b61554f97c.png">

<img width="571" alt="image" src="https://user-images.githubusercontent.com/49035567/236651781-29085b22-6934-4663-bc4b-e0113ecb272a.png">

<img width="570" alt="image" src="https://user-images.githubusercontent.com/49035567/236651787-42ab3398-23bd-4909-8a4e-c7c252065645.png">

Once created, import the the corresponding JSON files from `output/` to the appropriate collections.

<img width="574" alt="image" src="https://user-images.githubusercontent.com/49035567/236657227-d67c58fa-0ff0-44aa-b709-9da341d1fb4c.png">


