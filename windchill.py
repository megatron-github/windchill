"""
 *****************************************************************************
   FILE:         windchill.py

   DESCRIPTION:	The program takes inputs of temperature and wind speed
                  to calculate windchill

 *****************************************************************************
"""

def windchill_calculator():
    """ Windchill calculator starts here """
    print('Welcome to the windchill calculator!')

    temper = float(input('Enter the temperature: '))
    windspeed = float(input('Enter the wind speed: '))
    #input() both print and scan in python

    #5^6 = 5**6 in python
    windchill = float(35.74 + 0.6215 * temper - 35.75 * windspeed**0.16 + 
                      0.4275 * temper * windspeed**0.16)
    #Source: How Is Wind Chill Calculated? | Mental Floss
    #Cite: http://mentalfloss.com/article/26730/how-wind-chill-calculated

    print("At", temper, "degrees, with a wind speed of", windspeed, "miles" +
          " per hour,")
    print("the windchill is:", windchill, "degrees")

if __name__ == "__main__":
    windchill_calculator()
