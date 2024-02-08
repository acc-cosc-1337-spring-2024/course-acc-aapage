def get_options_ratio(options, total):
    ratio = float(options / total)
    return ratio

def get_faculty_rating(ratio):
    if ratio >= 1:
        print("Ratio is invalid; program could not produce rating. Rating should be less than 1.")
        rating = "Invalid"
    elif ratio >= 0.9:
        rating = "Excellent"
    elif ratio >= 0.8:
        rating = "Very Good"
    elif ratio >= 0.7:
        rating = "Good"
    elif ratio >= 0.6:
        rating = "Needs Improvement"
    else:
        rating = "Unacceptable"
    return rating