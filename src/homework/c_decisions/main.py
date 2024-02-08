import decisions

options = float(input("Input Option: "))
total = float(input("Input Total: "))
result = decisions.get_options_ratio(options, total)

print("Rating:",decisions.get_faculty_rating(result))
