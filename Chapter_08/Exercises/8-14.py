def save_car_info(manufacturer,model_number,**parameter):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model_number'] = model_number
    for key,value in parameter.items():
        car_info[key] = value
    return car_info

print()