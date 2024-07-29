def battery_is_ok(temperature):
 Check_temp(temperature)

def Check_temp(temperature):
  if temperature < 0 or temperature > 45:
    low_high_temperature(temperature)
    print('Temperature is out of range!')
    return False
  else:
    Check_temp(temperature)
 
