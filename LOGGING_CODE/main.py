import logging
from user_input_module import get_waste_type
from process_module import process_waste
from database_module import save_waste_data

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    handlers=[logging.FileHandler("smart_waste.log"), logging.StreamHandler()])

def main():
    logging.info("Smart Waste Management System started.")
    try:
        waste_type = get_waste_type()
        logging.info(f"User input received: {waste_type}")
        
        # Get quantity from user
        quantity = int(input("Enter the quantity of waste: "))  # Convert input to integer
        logging.info(f"User input received for quantity: {quantity}")

        waste_data = process_waste(waste_type, quantity)
        logging.info(f"Valid entry found: {waste_data}")
        
        save_waste_data(waste_data)
        logging.info("Data successfully saved to the database.")
    
    except ValueError:
        logging.error("Invalid input for quantity. Please enter a valid integer.")
    except Exception as e:
        logging.error(f"Exception occurred during input processing: {e}")
    
    logging.info("Smart Waste Management System finished.")

if __name__ == "__main__":
    main()
