import random

main_msg = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29"""

def main():
    while True:
        print(main_msg)
        try:
            user_answer = int(input())
            if 1 <= user_answer <= 2:
                break
            else:
                raise Exception('Incorrect format')
        except:
            print("Incorrect format")
    
    if user_answer == 1:
        marks = level_one()
    else:
        marks = level_two()

    # prompting user for saving the result
    print("Would you like to save your result to the file? Enter yes or no.")
    yes_answers = ['yes', 'YES', 'y', 'Yes']
    user_res = input()
    if user_res in yes_answers:
        print("What is your name?")
        username = input()
        file = open('results.txt', 'a', encoding="utf-8")
        if user_answer == 1:
            file.write(f"{username} {marks}/5 in level 1 (simple operations with numbers 2-9) \n")
        else:
            file.write(f"{username} {marks}/5 in level 2 (integral squares 11-29) \n")
        print('The results are saved in "results.txt".')

# if user selects difficulty 1        
def level_one():
    marks = 0  # counter for total right answers

    # loop for 5 questions
    for _ in range(5): 
        operator_list = ["+", "-", "*"]
        first_operand = random.randint(2,9)
        second_operand = random.randint(2,9)
        operator = operator_list[random.randint(0,2)]

        # finding the answer into result
        if operator == "+":
            result = first_operand + second_operand
        elif operator == "-":
            result = first_operand - second_operand
        elif operator == "*":
            result = first_operand * second_operand

        # displaying the prepared question
        print(first_operand, operator, second_operand)

        # user response to the question    
        while True:
            try:
                user_answer = int(input())
                break
            except:
                print("Incorrect format")

        # answer checking
        if user_answer == result:
            print("Right!")
            marks += 1
        else:
            print("Wrong!")

    # displaying marks        
    print("Your mark is {}/5.".format(marks))
    return marks

# difficulty 2
def level_two():
    marks = 0  # counter for total right answers

    # loop for 5 questions
    for _ in range(5): 
        num = random.randint(11, 29)

        # right answer
        result = num ** 2

        # displaying the randomly generated integer
        print(num)

        # user response to the question    
        while True:
            try:
                user_answer = int(input())
                break
            except:
                print("Incorrect format")

        # answer checking
        if user_answer == result:
            print("Right!")
            marks += 1
        else:
            print("Wrong!")
            
    # displaying marks        
    print("Your mark is {}/5.".format(marks))
    return marks

if __name__ == "__main__":
    main()
