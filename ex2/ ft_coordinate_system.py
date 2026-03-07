import math


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    
    point1 = (10, 20, 5)
    print(f"Position created: {point1}")
    d_point1_2 = point1[0]**2 + point1[1]**2 + point1[2]**2
    print(f"Distance between (0, 0, 0) and {point1}: {math.sqrt(d_point1_2):.2f}")
    #:.2f means 2 digits after the decimal
    
    print()
    string1 =  "3,4,0"
    arr1 = string1.split(",")
    print(f'Parsing coordinates: "{string1}"')
    arr1[0] = int(arr1[0])
    arr1[1] = int(arr1[1])
    arr1[2] = int(arr1[2])
    point2 = tuple(arr1)
    print(f"Parsed position: {point2}")
    d_point2_2 = point2[0]**2 + point2[1]**2 + point2[2]**2
    print(f"Distance between (0, 0, 0) and {point2}: {math.sqrt(d_point2_2):.1f}")
    
    
string2 = "abc,def,ghi"
print(f'\nParsing invalid coordinates: "{string2}"')

try:
    arr2 = string2.split(",")
    
    x = int(arr2[0])
    y = int(arr2[1])
    z = int(arr2[2])
    
    invalid_point = (x, y, z)

except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print("Error details - Type: ValueError, Args: (\"invalid literal for int() with base 10: 'abc'\",)")
    
print()
print("Unpacking demonstration:")
x, y, z = point2
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")