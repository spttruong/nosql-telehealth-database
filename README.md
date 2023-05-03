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



