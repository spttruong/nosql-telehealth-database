# NoSQL Telehealth Database

Link to YouTube Presentation:

## Business Case Overview

Suppose a healthcare business required a telehealth platform to conduct remote annual wellness visits. Their business model relies on an application that allows for the scheduling, administering, and tracking of patient and appointment data. Patients receive medical expertise from licensed medical providers who are also on the platform. The company tracks and confirms completed appointments through the application and use the appointment dispositions to bill medical groups regarding the completion of these appointments.

## Data Overview

This is a crude implementation of a noSQL (MongoDB) database for a fictional telehealth application. 

A noSQL database was chosen mainly because:

* they are scalable
* data model planning is less stringent and they are less rigid with data types (this can also be a detriment)
* quicker query times
* flexibility to modify various documents types later (e.g., what if the patient chart needs to capture additional data fields)

In general, this application would need to store user data and telehealth appointment data, including appointment dispositions for billing purposes and patient medical charts. The two kinds of users would be patients and the health providers providing the telehealth service. 

The data stored on this application includes the following document types: 

* `patient` - contains patient demographic data
* `patient_chart` - contains patient electronic medical records (EMRs)
* `provider` - contains data on employed health providers
* `appointment` - contains telehealth appointment data

You will notice within the actual database, there are actually only 3 document collections: `patients`, `providers`, and `appointments`. This is because the `patient_chart` document is embedded within the `patient` document (more on that later).

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

Any field that is type `array` can hold multiple values. For example, `patient.languages` can hold multiple string values corresponding to the languages the patient understands.

These diagrams were created using [Lucid.app](lucid.app).

### Data Disclaimers 

As stated, a Python script was used to generate the database and was mainly used to meet time constraints. The data was generated virutally at random with the intended goal to create purely fictional data. Any resemblance to real living entities are purely coincidental.

Additionally, due to how the Python script generated the data, there may exist some inconsistencies and discrepancies due to a lack of data validation rules.

For example, the system is supposed to be designed such that each appointment can have only one assigned health provider. However, as the data generator is trying to simulate the one-to-many relationship in which one provider conducts multiple appointments on the platform, while assigning appointments at random to the fictional providers, there are occurences in the database where multiple providers may have been inadvertently assigned to the same appointment.

Another example of this inconsistency is the fact that patients will keep track of a record of their past appointments by storing an array of `appointments` within the `patient` document. Again, the data generation script may have assigned the same appointment IDs to multiple patients.

Also, for the interest of time, the database backend does not implement any rules for data field validation such as:

* validating `email` addresses
* acceptable `phone` formats
* valid length for `insurance_id` or `insurance_payer_id`
* guaranteed uniqueness of document ids
* `date` format validation

Many of these fields are entered in as a `string` data type, which can lead to large variation of formats and lead to further inconsistencies due to human error.

In practice, there can be some front-end form validation rules applied on the client side of the application as users enter data into the application. Additional code can be written to keep the data consistent in the back-end as well. These ideas have not been fleshed out and are outside the scope of this project.

This may be one strong consideration for using a relational database instead because of the access to more stringent built-in data validation features.

## Repository User Guide and Set-up

### Python Overview

From a user perspective, if you want to just extract the mock data to play around with it, navigate to `output/` and download `appointments.json`, `patients.json`, and `providers.json`.

If you want to test out the data generation, you can execute `make_mock_data.py` located at the root of the repository from the command line:

`$ python make_mock_data.py`

The resulting JSON files can be found in `output/`

For reference, the repository looks like this:

![image](https://user-images.githubusercontent.com/49035567/236650602-16d711ff-0dfc-4cc4-8208-ca8192c250a5.png)

There are three main folders within the repo.

* `document_generator/` contains the scripts that generate fake patient, provider, and appointment data respectively
  * Note: the scripts are currently set up to generate 50 records for each document type 
* `output/` contains the output JSON files (the files created from `make_mock_data.py`
* `sample_documents/`, which contains templates/rough drafts of what a each document should look like

### Loading into MongoDB Compass

I am using a free MongoDB Atlas instance to store the data. I've also downloaded MongoDB Compass to manage and query the database. Therefore, the following steps will be demonstrated using the MongoDB Compass UI.

Click on the + icon to create a new database:

<img width="253" alt="image" src="https://user-images.githubusercontent.com/49035567/236650959-c71a6e78-ae2b-46db-b05a-b52376769f3f.png">

Name the database as well as the first collection within the database.

<img width="592" alt="image" src="https://user-images.githubusercontent.com/49035567/236651719-94854822-6a30-4523-bea9-eda6080fb303.png">

Proceed to create collections for the other document types as well.

<img width="256" alt="image" src="https://user-images.githubusercontent.com/49035567/236651753-05268306-317b-4ed7-bdbb-87b61554f97c.png">

<img width="571" alt="image" src="https://user-images.githubusercontent.com/49035567/236651781-29085b22-6934-4663-bc4b-e0113ecb272a.png">

Once created, import the the corresponding JSON files from `output/` to the appropriate collections.

<img width="574" alt="image" src="https://user-images.githubusercontent.com/49035567/236657227-d67c58fa-0ff0-44aa-b709-9da341d1fb4c.png">

Here is an example of the `patients` collection post-import. The second document has the embedded `patient_chart` document expanded.

<img width="760" alt="image" src="https://user-images.githubusercontent.com/49035567/236657892-9e78194b-7470-4c16-b260-c3dc1ce9a02a.png">

`providers` collection:

<img width="757" alt="image" src="https://user-images.githubusercontent.com/49035567/236657854-735aef23-3481-4839-9286-9e4d26e05945.png">

`appointments` collection:

<img width="758" alt="image" src="https://user-images.githubusercontent.com/49035567/236658174-4c3b2cd6-6afa-4ad0-9306-5e5a6d5da6e9.png">

## Database Use

### Sample Queries

#### Pulling Patient Demographic Info to Schedule Appointment

Query:

```
{
  name: "Adam Williams",
  date_of_birth: "1967-03-31"
}
```

Result:

<img width="672" alt="image" src="https://user-images.githubusercontent.com/49035567/236695425-3173aa55-9ce6-4168-bd7a-be237c395eca.png">

#### Provider Pulling Patient Health Chart to Update Vitals

Query: (same as above but using Project parameters to display the `patient_chart` document)

<img width="611" alt="image" src="https://user-images.githubusercontent.com/49035567/236695985-a957ccee-44d1-43eb-a11d-9d821c65e7d5.png">

Result:

<img width="1137" alt="image" src="https://user-images.githubusercontent.com/49035567/236695704-bd24a6fb-6f34-4e23-abf6-eb2af491fc9b.png">

#### Checking Patient's Most Recent Appointment for Billing Disposition

Query: (same as above but using Project parameters to display the `patient_chart.last_appointment_id`)

<img width="609" alt="image" src="https://user-images.githubusercontent.com/49035567/236695962-c541dbf0-3e08-434f-93e5-5afc31e43856.png">

Result:

<img width="350" alt="image" src="https://user-images.githubusercontent.com/49035567/236695944-ca1d652e-c3e8-427c-871d-c58d61bc1210.png">

#### Validating Total Number of Appointments Conducted by a Provider

This query could be used for auditing purposes.

Query (aggregation):

```
[
  {
    $match: {
      name: "Adam Gonzalez",
    },
  },
  {
    $project: {
      name: 1,
      appointments: 1,
      totalAppointments: {
        $size: "$appointments",
      },
    },
  },
]
```

Result:

<img width="284" alt="image" src="https://user-images.githubusercontent.com/49035567/236697128-714e688d-f4c1-404f-9976-996544327742.png">

#### Exploring Provider Credentialed Skills Distribution

This info can help company determine if they need to hire more providers of a specific credentialing still

Query (aggregation):

```
[
  {
    $group: {
      _id: "$credentialed_skills",
      count: {
        $sum: 1,
      },
    },
  },
]
```

Result:

<img width="1445" alt="image" src="https://user-images.githubusercontent.com/49035567/236698549-11bea768-229b-4c91-a7c9-d8fc77b4b177.png">

### Database Growth

From an end-user perspective, there would be some kind of front-end UI resembling a series of nested forms for providers, schedulers, administrators, and patients to view their data. Using that same UI, patients can edit their personal information, providers can conduct appointments and edit patient charts, and schedulers can modify appointment details.

The application would likely use MQL or some kind of API to create, read, update, and delete data. Here are some instances of scaling the database:

* new patients being entered into the `patients` collection by an administrator
* new providers are hired and provided user accounts begin conducting health appointments
* the number of appointments will continue to increase, and with each appointment conducted, the arrays `patient.appointments` and `provider.appointments` will continue to grow as to maintain appointment history
* `patient.patient_chart` can expand to contain more health information to accomodate needs of the company or patient (e.g., cholesterol level, blood type, allergies, immunizations)
* likewise, any of the other document types can have fields added to expand the amount of data collected
