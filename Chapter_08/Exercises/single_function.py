def show_sum(a, b):
    a_str,b_str = str(a),str(b)
    if a_str.isdigit() and b_str.isdigit():
        print(int(a_str) + int (b_str))
    else:
        print("Error. Please provide 2 numbers.")
