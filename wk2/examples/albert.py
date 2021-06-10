C = 299792458
E = "e = m * C^2.."

def main():
    mass = float(input("Enter kilos of mass: "))
    print(E)
    print("m =", mass, "kg")
    print("C =", f"{C:,d}", "m/s")
    energy = mass * (C**2)
    print(energy, "joules of energy!")

if __name__ == "__main__":
    main()