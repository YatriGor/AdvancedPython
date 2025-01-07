import logging

def get_waste_type():
    waste_type = input("Enter waste type (organic/recyclable): ")
    if waste_type not in ['organic', 'recyclable']:
        logging.warning(f"Invalid input received: {waste_type}")
        raise ValueError("Invalid waste type")
    return waste_type
