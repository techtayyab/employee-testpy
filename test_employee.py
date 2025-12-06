from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: somu\n"
        "Employee ID: E1001\n"
        "Department: IT\n"
        "Salary: $150000"
    )
    assert employee_details("somu", "E1001", "IT", 150000) == expected_output