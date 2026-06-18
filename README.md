# 🚀 Rocket Performance Calculator

## Objective

The Rocket Performance Calculator is a Python-based tool developed for rocketry enthusiasts, students, and aspiring aerospace engineers.

Its purpose is to help rocketeers quickly estimate key flight performance parameters of Level 1 and Level 2 rockets and compare the results with dedicated simulation software such as OpenRocket.

This project was created out of a passion for rocketry and space exploration. While it is not intended to replace professional simulation tools, it provides an educational way to understand the physics behind rocket flight and the calculations that drive rocket performance.

Whether you are preparing for a launch, learning aerospace engineering concepts, or simply fascinated by rockets, this calculator aims to be a useful companion for exploring and analyzing rocket behavior.

## Features

> ⚠️ This calculator is intended for educational purposes and preliminary performance estimation. Results should always be verified using dedicated simulation software such as OpenRocket before any launch.
## Future Development

This project is still under active development.

Future improvements may include:

- Aerodynamic drag modeling
- Stability analysis
- Center of Gravity (CG) calculations
- Center of Pressure (CP) calculations
- Static margin evaluation
- Recovery system analysis
- Wind drift prediction
- Flight trajectory visualization
- Graphical User Interface (GUI)
- Additional Level 2 and Level 3 flight analysis capabilities

As I continue learning aerospace engineering and software development, new features and improvements will be added to make the calculator more accurate and useful for the rocketry community.

## Author

Julien Vivian Gbadin Wo-Boussou

Aerospace Engineering Student

This project was built to share my passion for rocketry, space exploration, and engineering while creating a tool that may help fellow rocketeers better understand and analyze their rocket designs.

## How to Use

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/gbadinv-boop/rocket-performance-calculator.git
```

### 2. Navigate to the Project Folder

```bash
cd rocket-performance-calculator
```

### 3. Run the Calculator

```bash
python rocket_performance_calculator.py
```

### 4. Enter Your Rocket Data

The program will prompt you to enter:

- Liftoff Mass (kg)
- Propellant Mass (kg)
- Motor Designation
- Average Thrust (N)
- Burn Time (s)
- Air Density (kg/m³)
- Launch Rail Length (m)
- Launch Angle (deg)

### Example Input

```text
Liftoff Mass (kg): 6.5
Propellant Mass (kg): 1.8
Motor Designation: J350
Average Thrust (N): 350
Burn Time (s): 2.6
Air Density (kg/m³): 1.225
Launch Rail Length (m): 3
Launch Angle (deg): 85
```

### Example Output

```text
==============================
FLIGHT PERFORMANCE REPORT
==============================

Weight: 63.77 N
Thrust-to-Weight Ratio: 5.49
Initial Acceleration: 43.98 m/s²
Rail Exit Velocity: 16.25 m/s
Burnout Velocity: 114.35 m/s
Apogee: 815.10 m
Time to Apogee: 14.26 s
Mach Number: 0.33
Dynamic Pressure: 8.01 kPa

✅ TWR acceptable
⚠️ Rail exit velocity slightly low
✅ Subsonic flight
```

### Validation

Users are encouraged to compare the calculator results with simulations performed in OpenRocket to better understand the assumptions and limitations of simplified analytical calculations.
