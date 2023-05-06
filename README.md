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

### Document Relationship Diagram 

It may first be useful to visualize the document relationships similar to how we visualize entities in a relational database:

![image](https://user-images.githubusercontent.com/49035567/236638151-42ae8a73-2eb8-4506-8e5e-e2e907c3255a.png)

* Each `patient` has exactly one `patient_chart` that holds their medical data (one-to-one relationship) and vice versa. Each `patient_chart` holds the health data of exactly one `patient`.
* One `patient` may have a record of multiple `appointments` within their medical history (one-to-many relationship).
* Each `appointment` can be linked to one and only one `patient` as well as one and only one `provider`.
* One `provider` can conduct multiple `appointments` (one-to-many relationship).
* Multiple `appointments` can be linked to a single `patient_chart` (many-to-one relationship).

However, document relationships are a little different from relational database entity relationships as described in section, Data Model Design. Here is a more accurate way to view the document relationships:

![image](https://user-images.githubusercontent.com/49035567/236638353-213fdb4d-07a0-49e1-b40e-f6128eb7fc22.png)

* The `patient_chart` document is embedded within the `patient` document; in other words althought it is its own document, it is a part of the `patient` document
* The rest of the documents are related to one another via a referencing an `id` field

Here is the diagram with both relationships overlayed for perhaps a more holistic view of the database:

![image](https://user-images.githubusercontent.com/49035567/236638404-d8eb4258-f704-445c-bfe0-792ca026a578.png)




