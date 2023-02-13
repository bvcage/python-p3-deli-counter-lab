def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line = ["The line is currently:"]
        for n in range(0, len(katz_deli)):
            line.append(f"{n+1}. {katz_deli[n]}")
        print(*line)

def take_a_number():
    pass

def now_serving():
    pass

