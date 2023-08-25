import shapes

def main():
    r1_area = shapes.area_rectangle(4,5)
    print(f"The area of a rectangle with sides 4 and 5 is {r1_area}")

    r1_perimeter = shapes.perimeter_rectangle(4,5)
    print(f"The perimeter of a rectangle with sides 4 and 5 is {r1_perimeter}")

    t1_area = shapes.area_triangle(2.3, 4.5)
    print(f"The area of a triangle with base 2.3 and height 4.5 is {t1_area}")

    t1_perimeter = shapes.perimeter_triangle(2.3, 4.5, 6.7)
    print(f"The perimeter of a triangle with sides 2.3, 4.5, and 6.7 is {t1_perimeter}")

if __name__== "__main__":
  main()