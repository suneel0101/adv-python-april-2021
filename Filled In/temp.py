def convert_temp(temp, from_temp='Celsius'):
    if from_temp == 'Celsius':
        if temp < -273.15:
            return 'Invalid temperature'
        return ((9/5) * temp) + 32
    else:
        return (temp - 32) * 5/9