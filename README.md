# NoSQL Telehealth Database

**Description:**

The Python scripts in this repository generate sample data for a MongoDB database that stores data relating to a ficitonal telehealth platform. The data included on such an application includes: patient demographic data, patient electronic medical records (EMRs), telehealth appointment data, and employed health provider data.

## Data Model Design

This database utilizes a a combination of both **embedded** and **normalized** data models. 

For more information on both of of these models, you can refer to [MongoDB's documenation](https://www.mongodb.com/docs/) on [Data Model Design](https://www.mongodb.com/docs/manual/core/data-model-design/#embedded-data-models).

### Embedded Data Model

As the name suggests, in the embedded data model, documents "contain" other documents. That is to say, they have other documents embedded inside them. This model is particularly useful for one-to-one document relationships where a user querying a document would often query for another related document. The embedded model also supports many-to-one relationships where multiple documents can be embedded within a single document. However, this runs the risk of creating documents that are too large to manage.

### Normalizeed Data Model

In the normalized data model, documents contain **references**, usually in the form of an `id` field to refer to other documents. This is different from the embedded data model in the sense that different document types are kept in separate collections and are linked via the aforementioned reference field. This is similar to the concept of SQL foreign keys, which link entities in one table to another table in the database.

## Document Collections

There are 4 types of documents within the database:

1. `patient`
2. `patient_chart`
3. `provider`
4. `appointment`

* Each `patient` has exactly one `patient_chart` that holds their medical data (one-to-one relationship) and vice versa. Each `patient_chart` holds the health data of exactly one `patient`.
* One `patient` may have a record of multiple `appointments` within their medical history (one-to-many relationship).
* Each `appointment` can be linked to one and only one `patient` as well as one and only one `provider`.
* One `provider` can conduct multiple `appointments` (one-to-many relationship).
* Multiple `appointments` can be linked to a single `patient_chart` (many-to-one relationship).

Here is an document relationship diagram to better visualize the data. 

It may first be useful to visualize the document relationships

While extremely similar to the traditional entity relationship diagram used to describe SQL databases, this diagram is slightly different in that the lines connecting each document also states whether or not the document(s) have an embedded relationship or a reference type of relationship.



