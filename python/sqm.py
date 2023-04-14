def alg(base, power, mod):
    print()

    res = 1
    for i in power[2:]:
        if i == "0":
            print(f" sq:  {res}^2 = {(res**2) % mod}")
            res = (res ** 2) % mod
        elif i == "1":
            print(f" sqm: {res}^2*{base} = {(res**2*base) % mod}")
            res = (res ** 2 * base) % mod

    print("\n", f"result is: {res} mod {mod}")
    

if __name__ == "__main__":
    print()
    alg(int(input(" * enter base: ")),bin(int(input(" * enter power: "))), int(input(" * enter mod: ")))

