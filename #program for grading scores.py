#program for grading scores
score = int(input("Enter your score: "))
if (score>=70 and score<=100):
    print("Your grade is A.")
elif (score>=60 and score<=69):
    print("Your grade is B.")
elif (score>=50 and score<=59):
    print("Your grade is C.")
elif (score>=40 and score<=49):
    print("Your grade is D.")
elif (score<=39):
    print("FAIL. Take suprementary exam.")
else:
    ("Enter valid score!!!")