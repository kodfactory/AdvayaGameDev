fruits = [
    {'que' : 'Please select which is a fruit ?: a) mango, b) tree ,c) bike,d) computer\n', 'correct_ans':'a', 'points': 10},
    {'que' : 'Select the Health Fruit for Older People ? : a) buble gum , b) cocacola, c) caroot,d)beer\n', 'correct_ans':'c', 'points': 10},
    {'que' : 'Select the best Fruit to eat in Morning time ? : a) Guava, b) pepsi ,c) jungle,d) river\n', 'correct_ans':'a', 'points': 10}
]

cricket = [
    {'que' : 'Who won the 2011 World Cup? a) India, b) Africa, c) Australia, d) Bantwa \n', 'correct_ans':'a', 'points': 20},
    {'que' : 'Who is highest run scorer in cricket history? :  a) Kohli, b) De Villiars ,c) Sachin, d) Dhoni\n', 'correct_ans':'c', 'points': 20},
    {'que' : 'Who is best bowoler in 2020 ?  a) Bumrah, b) Wasim Akram,  c) Salim Malik, d) Babu rav\n', 'correct_ans':'a','points':  20}
]

actors = [
    {'que' : 'Who is the best actor 2018 ? : a) Mike Tysson , b) Khan, c) Bruce lee, d) Elia\n', 'correct_ans':'a', 'points': 50},
    {'que' : 'Who is the best actor 2019 ? : a) Rambo, b) Arnold , c) Denzel, d) Donnie Yen\n', 'correct_ans':'a', 'points': 50},
    {'que' : 'Who is the best actor 2020 ? : a) Michael Jai White, b) Steven Seagal, c) Scott, d) Idris\n', 'correct_ans':'a', 'points': 50}
]

players = [
    {'que' : 'Who was the best player in 2018 ? : a) Alfred Khoza, b) Manuel Fanuel, c) Peter Clark d) Andrew Clark\n', 'correct_ans':'b', 'points': 100},
    {'que' : 'Who was best player in 2019 ? :  a) Neymar, b) Ronaldo ,c) Delima, d) Elia\n', 'correct_ans':'b', 'points': 100},
    {'que' : 'Who is the best player in 2020 ?  a) Peter Sosi, b) Rick Ma,  c) Adam Mo, d) Nassib KO\n', 'correct_ans':'b','points':  100}
]

all_category = {'Fruits': fruits, 'Sports' : cricket, 'Hollywood' : actors, 'Football': players}

print("*"*50)
print("*             Welcome to Quiz Game               *")
print("*"*50)
total_points = 0

def start_game():
    global total_points
    for category, all_questions in all_category.items():
        print(f"Let's start with {category}...")
        for question in all_questions:
            que, correct_ans, points = question['que'],question['correct_ans'],question['points']
            
            user_ans = input(que)
            if user_ans.lower() == correct_ans:
                print(f"You are correct, {points} points!")
                total_points += points
            else:
                print("Incorrect answer...!!")

    print(f"Your total Score is {total_points}!")

# def start_game():
#     global total_points
#     print("Below are list of Categories, Choose the correct option: ")
#     for category in all_category.keys():
#         print(category)
#     user_choice = input("Type the name of category: ")
    
#     print(f"Let's start with {user_choice}...")
#     for question in all_category[user_choice]:
#         que, correct_ans, points = question['que'],question['correct_ans'],question['points']
        
#         user_ans = input(que)
#         if user_ans.lower() == correct_ans:
#             print(f"You are correct, {points} points!")
#             total_points += points
#         else:
#             print("Incorrect answer...!!")

#     print(f"Your total Score is {total_points}!")

start_game()