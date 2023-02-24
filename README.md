# CarModelSearchAPIService
The single endpoint API for retrieving car models by make and year.

Please contact mikesungunkim@gmail.com for any inquiries.

## Installation 
___ 
Warning: These steps have been verified only with Mac.
1. Clone this project to your local directory.
```bash
git clone https://github.com/mikesukim/CarModelSearchAPIService.git
```
2. Run Docker Desktop (Docker installation requires if Docker-desktop is not installed) and leave it running.
3. Enter this project's directory through terminal/Powershell
```bash
cd CarModelSearchAPIService
```
4. Build the CarModelSearchAPIService container by running docker-compose.yml file. This step also run testings. If failed to pass test cases, then build will fail. 
```bash
docker-compose build
```
5. Run the container.
```bash
docker-compose up
```
6. Make sure the server is up and running by entering http://localhost:8000 in a browser/Postman.
## API
___
### Request
 `GET /models/{model}/{year}`
```bash
 curl -i http://localhost:8000/models/Ferrari/2018
```
### Response
```
Search success! 2 model(s) are found: 
488 GTB, 488 Spider
```


## Implementation detail
___
### 1) Dependencies
- Flask
- Pytest

### 2) Possible future improvement
- Adding dependency Injection(DI) framework.
    - Currently, DI is not used, to follow the suggestion of using standard python libraries as much as possible.
- Separating into multiple modules/classes.
    - Currently, all logic codes are in one place, app.py.
    - However these centralized codes need to be separated into multiple modules/classes, so each module/class can serve one purpose, which makes it easy to maintain, and scale for future development. 
    - Since DI was not used for this challenge, I decided to centralize all logic/codes into one place.
    - Here are a few possible modules/classes for this project
        - Response_handler → Module for generating flask responses.
        - Cvs_interface → Module for dealing with CSV files. it knows how to read, convert, and check the metadata of the CVS file.