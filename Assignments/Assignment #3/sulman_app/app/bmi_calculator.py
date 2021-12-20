def BMI_calculator(weight, height):
    """ Function to calculate the BMI of an individual given their respective weight (lb) and height (in)"""
    # Calculate BMI using lb / inches equation
    bmi = ((weight)/(height * height)) * 703

    return bmi
