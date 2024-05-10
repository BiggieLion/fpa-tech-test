# FP Alpha tech test

Table of content
- [FP Alpha tech test](#fp-alpha-tech-test)
  - [Requirement](#requirement)
  - [Dependencies](#dependencies)
  - [How to install](#how-to-install)
  - [How to use](#how-to-use)
  - [Routes and endpoints](#routes-and-endpoints)
  - [How to change the text](#how-to-change-the-text)
  - [Author](#author)

## Requirement

This is a flask service for receiving raw data *(like the response sent by a IA tool)* and mapping that to a JSON object *(mockup expressed in the response.json)*

## Dependencies

All the dependencies are listed in the **requirements.txt** file

## How to install

1. Install Python v3Install the dependencies from the requirements.txt
2. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
3. Install all the dependencies from **requirements.txt** file
4. Run ```flask run``` to run the project.

## How to use

In order to test and see how the service works you should do the following steps:

1. Install [Postman](https://www.postman.com/downloads/)
2. Import the collection that is in the **FP Alpha Tech Test.json** file, it has the vars in the env vars.
3. Run the service

## Routes and endpoints

The service has the following endpoints to request:

1. ```GET /api/ping```
   - Method: Get
   - Purpose: To test if the service is working
   - Response: A message with the data *pong*
2. ```GET /api/json```
   - Method: Get
   - Purpose: To get the JSON Object as requested
   - Body: The endpoint accept the following body:
   - ```JSON { "data": {{text_x}} }``` where *x* is the number of the variable(one, two, three and four)

## How to change the text

If you want to change the value of the text you must go to *Scripts* tab in the *GET /api/json* request, then, change the value of the variable you want to change

## Author

Jair León (BiggieLion)

- [LinkedIn](https://www.linkedin.com/in/jairleon/)
- [GitHub](https://github.com/BiggieLion/)
