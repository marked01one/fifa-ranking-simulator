<h1 align="center">FIFA Rankings Simulator</h1>


An online simulator that allows users to create fictional campaigns of international FIFA football tournaments. 


Create an instance of all countries' FIFA World Rankings and simulate through fantasy tournaments and watch how their FIFA points and rankings change over time!

<h1 align='center'>Synopsis</h1>

### Overview
FIFA World Rankings is a unified system of points developed to rank the relative footballing ability between all FIFA member nations. Despite criticisms from fans regarding the accuracy of the rankings, it has been used extensively by FIFA and their associate confederations for seeding teams during cup competitions and qualifiers

### Current Model
The latest model used for calculating the FIFA rankings of each country were created after the 2018 FIFA World Cup. For more information on the model and how it works, refer to the link below:

<div align='center'>

**[Revision of the FIFA World Ranking](https://digitalhub.fifa.com/m/f99da4f73212220/original/edbm045h0udbwkqew35a-pdf.pdf)**
</div>

<h1 align="center">Project Details</h1>

### Overview
The project is split into multiple components, including:
* Web application:
  * API
  * User interface client
  * Databases
* Data analysis & extraction:
  * Jupyter Notebooks & Pandas

**NOTICE:** *All information about the project in this section are subject to change*


<h2 align="center">API</h2>

Base URL during development: `http://localhost:8000`

### Method: `GET` 
* `/countries` 
  * Return data about all countries
* `/confederations` 
  * Return data about all confederations
* `/countries/confederation?id={int:id}`
  * Return a list of all countries belonging to a specific confederation ID
  * **Example:**
```python
http://localhost:8000/countries/confederation?id=7  
# Returns data of all countries belonging to confederation 7, which is UEFA
```
* `/countries/fifa?code={fifa_code}`
  * Return data for country with the specific 3-letter FIFA abbreviation given
  * **Example:** 
```python
http://localhost:8000/countries/fifa?code=VIE  
# Returns data for country with code VIE, which is Vietnam
 ```

