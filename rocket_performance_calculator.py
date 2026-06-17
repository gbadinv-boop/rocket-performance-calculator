#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def get_rocket_input():
    print("==================================================")
    print("           ROCKET PERFORMANCE CALCULATOR          ")
    print("==================================================\n")
    print("Hello dear rocketeers and welcome to the Rocket Performance Calculator!")
    print("Ready to see how your rocket will perform?")
    print("This calculator analyzes key flight parameters such as altitude, velocity,")
    print("acceleration, and stability using your rocket's design data.")
    print("Please enter your rocket specifications below and let the simulation begin!\n")
    
    print("--- Mass properties ---")
    liftoff_mass = float(input("liftoff mass (kg): "))
    propellant_mass = float(input("propellant mass (kg): "))
    print("\n")
    
    print("--- MOTOR DATA ---")
    motor_designation = str(input("Motor designation: "))
    average_thrust = float(input("Average thrust (N): "))
    burn_time = float(input("Burn time (s): "))
    print("\n")
    
    print("--- AERODYNAMICS ---")
    air_density = float(input("Air Density (kg/m3): "))
    print("\n")
    
    print("--- LAUNCH CONDITIONS ---")
    launch_rail_length = float(input("Launch rail Length (m): "))
    launch_angle = float(input("Launch angle (deg): "))
    
    dry_mass = liftoff_mass - propellant_mass
    payload_mass = 0.0 
    
    return (liftoff_mass, dry_mass, propellant_mass, payload_mass, 
            motor_designation, average_thrust, burn_time, air_density, 
            launch_rail_length, launch_angle)

def get_motor_designation(motor_designation):
    return motor_designation

def get_liftoff_mass(liftoff_mass):
    return liftoff_mass

def calculate_weight(liftoff_mass):
    weight = liftoff_mass * 9.81
    return weight

def calculate_twr(average_thrust, weight):
    twr = average_thrust / weight
    return twr

def calculate_mass_flow_rate(propellant_mass, burn_time):
    mass_flow_rate = propellant_mass / burn_time
    return mass_flow_rate

def calculate_acceleration(weight, liftoff_mass, average_thrust):
    acceleration = (average_thrust - weight) / liftoff_mass
    return acceleration

def calculate_rail_exit_velocity(acceleration, launch_rail_length):
    rail_exit_velocity = math.sqrt(2 * acceleration * launch_rail_length)
    return rail_exit_velocity

def calculate_burnout_time(burn_time):
    return burn_time

def calculate_max_velocity(acceleration, burn_time):
    maximum_velocity = acceleration * burn_time
    return maximum_velocity

def calculate_apogee(acceleration, burn_time, maximum_velocity):
    g = 9.81
    h_burn = 0.5 * acceleration * (burn_time ** 2)
    h_coast = (maximum_velocity ** 2) / (2 * g)
    apogee = h_burn + h_coast
    return apogee

def generate_report(motor_designation, liftoff_mass, weight, twr, acceleration, 
                    rail_exit_velocity, maximum_velocity, apogee, time_to_apogee, 
                    mach, maximum_dynamic_pressure):
    print("\n" + "=" * 50)
    print("           FLIGHT PERFORMANCE REPORT")
    print("=" * 50)
    print(f"\nMotor Designation: {motor_designation}")
    print(f"Liftoff Mass: {liftoff_mass:.2f} kg")
    
    print("\n------------------ PROPULSION -------------------")
    print(f"Weight: {weight:.2f} N")
    print(f"Thrust-to-Weight Ratio: {twr:.2f} ")
    
    print("\n------------------ PERFORMANCE ------------------")
    print(f"Initial Acceleration: {acceleration:.2f} m/s2")
    print(f"Rail exit velocity: {rail_exit_velocity:.2f} m/s")
    print(f"Maximum velocity: {maximum_velocity:.2f} m/s")
    print(f"Apogee: {apogee:.2f} m")
    print(f"Time to Apogee: {time_to_apogee:.2f} s")
    
    print("\n------------------ AERODYNAMICS ------------------")
    print(f"Maximum Mach Number: {mach:.2f} ")
    print(f"Maximum Dynamic Pressure: {maximum_dynamic_pressure:.2f} Kpa")
    
    print("\n------------------ MISSION STATUS ----------------")
    if twr >= 5:
        print("✅ TWR acceptable")
    else:
        print("⚠️ TWR below recommended value")
        
    if rail_exit_velocity >= 20:
        print("✅ Rail exit velocity acceptable")
    else:
        print("⚠️ Rail exit velocity too low")
        
    if mach < 0.8:
        print("✅ Subsonic flight")
    else:
        print("⚠️ Approaching transonic regime")
        
    print("\n" + "=" * 50)
    print("           END OF FLIGHT ANALYSIS")
    print("=" * 50)


# --- MAIN EXECUTION FLOW ---

# 1. Get user inputs
(liftoff_mass, dry_mass, propellant_mass, payload_mass, 
 motor_designation, average_thrust, burn_time, air_density, 
 launch_rail_length, launch_angle) = get_rocket_input()

print("\n")
print("CALCULATING...")

weight = calculate_weight(liftoff_mass)
twr = calculate_twr(average_thrust, weight)
acceleration = calculate_acceleration(weight, liftoff_mass, average_thrust)
rail_exit_velocity = calculate_rail_exit_velocity(acceleration, launch_rail_length)
maximum_velocity = calculate_max_velocity(acceleration, burn_time)
apogee = calculate_apogee(acceleration, burn_time, maximum_velocity)

time_to_apogee = burn_time + (maximum_velocity / 9.81)

mach = maximum_velocity / 343.0 
maximum_dynamic_pressure = 0.5 * air_density * (maximum_velocity ** 2) / 1000.0 

generate_report(
    motor_designation, liftoff_mass, weight, twr, acceleration, 
    rail_exit_velocity, maximum_velocity, apogee, time_to_apogee, 
    mach, maximum_dynamic_pressure
)


# In[ ]:




