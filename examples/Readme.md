# Demos

These demos were part of a presentation, the slides are published here: [speakerdeck](https://speakerdeck.com/emanum/wiederverwendbare-software-komponenten-mit-elo-und-python)

## How to run the demos locally

```bash
pipenv install
pipenv shell
juptyer notebook
```

Then open the notebook and run the cells. 

Please note that you need access to a running
elo indexserver to run the demos. The credentials are loaded from a .env file.

To get access to an indexserver, get in contact with [ELO](https://www.elo.com/de-at.html) and buy a license.
Or use the free open source version which can be downloaded [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Sales Trend Analysis

This demo loads data via the elo-indexserver-client and post processes them (cleanup, transformation) in order to
use the data for various other libraries as a proof of concept. Here we use pandas to explore the data and seaborn to
generate a simple barchart. Afterwards, we generate a pdf via reportlab.

## DataImport

This demos uses a sales dataset from kaggle to demonstrate how to import data into the indexserver. 

## Run via docker (compose)

Set the required env variables:
```bash
SET ELO_IX_URL=http://...
SET ELO_IX_USER=...
SET ELO_IX_PASSWORD=...
```


Build and run:
```bash
docker-compose up --build dataimport
```


## Common issues

### 500 error without any message

This could be due to the wrong URL. Make sure to use the URL for the rest API not the generic URL which is used in the 
elo client.

wrong: `http://localhost:8080/ix-Archive/ix`
correct: `http://localhost:8080/ix-Archive/rest`

This would result in the following error message on the server:
```log
http-nio-9090-exec-1 http-7298485 (IXServlet.java:611)       - Exception 
java.io.IOException: org.json.JSONException: JSONObject["clazz"] not found.
```
