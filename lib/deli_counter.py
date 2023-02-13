def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line = ["The line is currently:"]
        for n in range(0, len(katz_deli)):
            line.append(f"{n+1}. {katz_deli[n]}")
        print(*line)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli[0]
        del katz_deli[0]
        print(f"Currently serving {serving}.")

