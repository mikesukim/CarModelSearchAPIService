import pytest
from unittest import TestCase
from src import app

def test_success_generating_dict():
    rows = [
        ["McLaren", "570GT, 570S, 720S", "2018"],
        ["Ferrari", "488 GTB, 488 Spider", "2018"]
    ]
    cars = app.convert_car_rows_to_dict(rows)

    # lower() is repeated for better testing readability
    assert "McLaren".lower() in cars
    assert "2018" in cars["McLaren".lower()]
    assert cars["McLaren".lower()]["2018"] == ["570GT", "570S", "720S"]

    assert "Ferrari".lower() in cars
    assert "2018" in cars["Ferrari".lower()]
    assert cars["Ferrari".lower()]["2018"] == ["488 GTB", "488 Spider"]

def test_failure_generating_dict():
    rows = [
        # maker data went missing
        ["570GT, 570S, 720S", "2018"],
        ["Ferrari", "488 GTB, 488 Spider", "2018"]
    ]
    with pytest.raises(Exception):
        cars = app.convert_car_rows_to_dict(rows)

def test_success_reading_testing_cvs_file():
    filename = "cars.csv"
    rows = app.read_cvs_into_rows(filename)
        
def test_failure_reading_cvs_file():
    filename = "file_that_does_not_exist.cvs"
    with pytest.raises(Exception):
        cars = app.read_cvs_into_rows(filename)

def test_success_get_model():
    make = "McLaren"
    year = "2018"
    response = app.get_model(make, year)
    assert response.status_code == 200

def test_get_model_failure_due_to_no_result():
    make = "Hyundai"
    year = "2018"
    response = app.get_model(make, year)
    assert response.status_code == 400

def test_get_model_failure_due_to_wrong_input_format():
    # year is some random string
    make = "Hyundai"
    year = "some_random_string"
    response = app.get_model(make, year)
    assert response.status_code == 400