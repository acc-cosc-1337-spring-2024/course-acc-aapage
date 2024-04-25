from dictionary import *

widgets = {}

while True:
    p = True
    while p:
        valid_responses = ['1', '2', '3']
        response = input("""Menu:
                         1 - Add or Update Item
                         2 - Delete Item
                         3 - Exit
                         Input: """)
        if response not in valid_responses:
            print("Please input a valid response")
        else:
            p = False
    
    while response == '1':
        widget_name = input("Please input a widget name: ")
        quantity = input("Now input a quantity: ")
        quantity = int(quantity)
        add_inventory(widgets, widget_name, quantity)
        print("Your widget has been added, and your dictionary now looks like this:")
        print(widgets)
        response = None

    while response == '2':
        widget_name = input("Please input the name of the widget you would like to remove: ")
        print(remove_inventory_widget(widgets, widget_name))
        response = None

    while response == '3':
        print("Now exiting program.")
        exit()

        



# This code belongs to a different assignment
# import sets

# prog1 = {"Student1", "Student2", "Student3"}
# prog2 = {"Student3", "Student4", "Student5"}

# while True:
#     p = True
#     while p:
#         valid_responses = [1, 2, 3, 4, 5]
#         response = input("""Menu:
#                          1 - Students who took prog1 and prog2
#                          2 - Students who took prog1 or prog2
#                          3 - Students who took prog1
#                          4 - Students who took prog2
#                          5 - Exit
#                          Input: """)
#         response = int(response)
#         if response not in valid_responses:
#             print("Please select a valid response. [1, 2, 3, 4, 5]")
#         else:
#             p = False

#     while response == 1:
#         print(f'The students who took prog1 and prog2 were {sets.get_students_who_took_prog1_and_prog2(prog1, prog2)}')
#         break
#     while response == 2:
#         print(f'The students who took prog1 or prog2 were {sets.get_students_who_took_prog1_or_prog2(prog1, prog2)}')
#         break
#     while response == 3:
#         print(f'The students who took prog1 were {sets.get_students_who_took_prog1_not_prog_2(prog1, prog2)}')
#         break
#     while response == 4:
#         print(f'The students who took prog2 were {sets.get_students_who_took_prog2_not_prog_1(prog1, prog2)}')
#         break
#     while response == 5:
#         print("Exiting the program.")
#         exit()