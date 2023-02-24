import csv
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_main_page() -> Response:
    return Response (
            "Welcome to CarModelSearchAPIService!",
            status = 200
    ) 

@app.route('/models/<make>/<year>', methods = ['GET'])
def get_model(make:str = None, year:str = None) -> Response:

    # check input type
    try:
        int(year)
    except:
        return Response(
            "Year should be in number format.",
            status = 400
        )
    
    # convert CVS to nested dictionary 
    # structure of nested dictionary is described at convert_car_rows_to_dict() description.
    try:
        rows = read_cvs_into_rows('cars.csv')
        cars = convert_car_rows_to_dict(rows)
    except:
        return Response(
            "Exception occures when converting CVS to dict.",
            status = 400
        )
    
    # search for models
    make_in_lowercase = make.lower()
    if not make_in_lowercase in cars or not year in cars[make_in_lowercase]:
        return Response(
            "No model found for the year: " + year + ", make: " + make,
            status = 400
        )
    
    models = cars[make_in_lowercase][year]
    models_in_str = ", ".join(model for model in models)
    return Response(
        "Search success! " + str(len(models)) + " model(s) are found: \n" + models_in_str,
        status = 200
    )

'''
Read CVS file and return rows(list type). 
'''
def read_cvs_into_rows(cvs_file_name:str) -> list:
    rows = []
    try:
        with open(cvs_file_name, newline='') as csv_file:
            for row in csv.reader(csv_file, delimiter=','):
                rows.append(row)
    except:
        raise Exception('reading csv file has failed.')
    return rows

'''
Convert CVS car rows to nested Dictionary.
structure of the dictionary is as follow.
{ <make> :
    { <year> : 
        [model 1, model 2...]
    } 
}
'''
def convert_car_rows_to_dict(rows) -> dict:
    cars = dict()
    for i,row in enumerate(rows):
        # check if each row is in correct format
        make,year,model = "","",[]
        try:
            make,model,year = row[0].lower(), row[1].split(", "), row[2]
        except:
            raise Exception('wrong format of car data.')
        
        # build dictionary 
        if make in cars:
          if year in cars[make]:
            cars[make][year].extend(model)    
          else:
            cars[make][year] = model
        else:
            cars[make] = { year : model}
    
    return cars
        

if __name__ == "__main__":    
    app.run(debug=True, port='8000' ,host='0.0.0.0')