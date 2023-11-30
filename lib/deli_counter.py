def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
        return;
    katz_deli = [f'{katz_deli.index(name) + 1}. {name}' for name in katz_deli ]
    print(f"The line is currently: {' '.join(katz_deli)}")

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {katz_deli.index(name) + 1} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
        return;
    user = katz_deli.pop(0)
    print(f'Currently serving {user}.') 
