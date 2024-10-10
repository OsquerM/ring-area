#Variables
grayArea = 0
PI = 3.14
def run(z: float) -> float:
    # TODO
    global grayArea 
    radioCircBlanco = z / 2
    areaCircBlanco = PI * radioCircBlanco ** 2
    radioCircGris = z + radioCircBlanco 
    areaCircGris = PI * radioCircGris ** 2
    grayArea = areaCircGris - areaCircBlanco 
    return grayArea


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(grayArea)
