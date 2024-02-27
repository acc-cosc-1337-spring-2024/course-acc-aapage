import strings

while True:
    response = int(input("""
    1 - Hamming Distance
    2 - DNA Compliment
    3 - Exit
    Input [1,2,3]: """))
    valid_responses = [1, 2, 3]

    if response not in valid_responses:
        print("Please input a valid response from the list [1,2,3].")
        continue

    elif response == 1:
        while True:
            #collect strings for hamming distance
            dna1 = str(input("Input First Sequence: "))
            dna2 = str(input("Input Second Sequence: "))

            # compare lengths of strings
            if len(dna1) != len(dna2):
                print("Please input strings of equal length.")
                continue
        
            hamming_distance = strings.get_hamming_distance(dna1, dna2)
            print(f'\nThe hamming distance of {dna1} and {dna2} is {hamming_distance}')
            break
        continue

    elif response == 2:
        dna = str(input("Input DNA sequence: "))
        compliment = strings.get_dna_compliment(dna)
        print(f'\nThe compliment of {dna} is {compliment}')
        continue
    
    elif response == 3:
        print("Thank you for playing.")
        break