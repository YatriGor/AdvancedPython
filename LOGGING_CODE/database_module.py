def save_waste_data(waste_data):
    # This is where you would typically save to a database.
    # For simplicity, let's assume we are saving to a file.
    with open("waste_data.txt", "a") as f:
        f.write(f"{waste_data}\n")
