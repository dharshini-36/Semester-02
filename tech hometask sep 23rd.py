#1
'''broadband_plans={
    "basic":{
        "speed":"30 mbps",
        "price":"600/month"
        },
    "standard":{
        "speed":"50 mbps",
        "price":"1000/month"
        },
    "premium":{
        "speed":"150 mbps",
        "price":"1500/month"
        }
    }
latest_bills={
    "user1": "600",
    "user2": "1500",
    "user3": "1000"
    }


def check_broadband_plan(plan_name):
    if plan_name in broadband_plans:
        plan=broadband_plans[plan_name]
        print(f"your plan {plan_name} offers {plan['speed']} for {plan['price']}.")
        print("\nAdditionally you will get free access for OTT platforms like AMAZON PRIME,HOTSTAR,ZEE5.....")
    else:
        print("Sorry, that plan is not available....):")
def check_latest_bills(user_id):
    if user_id in latest_bills:
        print(f"Your latest bill amount is: {latest_bills[user_id]}.")
    else:
        print("Sorry, we couldn't find your billing information......")

def report_issue(issue):
    print("Thank you for reporting the issue.")
    print("\nOur team will support you and rectify we will try to rectify the issue soon.....")


def greet():
    print("WELCOME TO BROADBAND SERVICES!!")
    print("\nYOU CAN ASK ABOUT YOUR BROADBAND PLANS,CHECK YOUR LATEST BILLS,REPORT ISSUES")

    while True:
        print("\n What kind of service you need..")
        print("1. Check the broadband plans.")
        print("2. Check your latest  bills.")
        print("3. Report any issues.")
        print("4. Exit.")

        choice=int(input("Enter your choice(1 or 2 or 3): "))
        if choice==1:
            plan_name=input("Enter your broadband plan(basic,standard,premium): ")
            check_broadband_plan(plan_name)
        elif choice==2:
            user_id=input("Enter your user id: ")
            check_latest_bills(user_id)
        elif choice==3:
            issue=input("What problem you are facing?: ")
            report_issue(issue)
        elif choice==4:
            print("Thank you choosing our Broadband service!!")
            quit()
        else:
            print("Invalid choice....please choose from (1,2,3,4)")
            
greet()'''

#2

import random
def conduct_quiz(questions):
    score=0
    total_questions=len(questions)
    for ques,ans in questions.items():
        print(ques)
        user_ans=input("Enter your answer: ")
        if user_ans.lower()==ans.lower():
            print("Correct!!!")
            score+=1

        else:
            print(f"wrong answer, correct answer is: {ans}")
    print(f"\n your score is: {score}/{total_questions}")

def main():
    print("WELCOME TO THE QUIZ...ALL THE BEST:)")
    quiz_questions={
    "Is string mutable": "no it is immutable",
    "How is list created": "it is created using square bracket",
    "How to get last element in a list": "using negative indexing",
    "
    }
    conduct_quiz(quiz_questions)
main()










        
