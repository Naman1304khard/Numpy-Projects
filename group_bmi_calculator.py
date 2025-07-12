import numpy as np

name = np.array(["Alice", "Bob", "Charlie", "David", "Eva"])
height = np.array([1.65, 1.80, 1.75, 1.60, 1.70]) #in meters
weight = np.array([55, 85, 77, 60, 68])  #in kilogram

#Calculate BMI
bmi = weight / (height **2)
bmi = np.round(bmi,2)

# Print BMI vlaues
print( "BMI values:")
for name, value in zip(name, bmi):
    print(f"{name}: {value}")

# Classify BMI
def classify_bmi(value):
    if value < 18.5:
        return "Underweight"
    elif value < 25:
        return "Normal"
    elif value < 30:
        return "Overweight"
    else:
        return "Obese"
    
 # Vectorized classification using list comprehension
bmi_classes = np.array([classify_bmi(val) for val in bmi])

#Print Classifcation
print("\n BMI Classification:")
for name, value, category in zip(name, bmi, bmi_classes):
    print(f"{name}: BMI = {value}, Category = {category}")
