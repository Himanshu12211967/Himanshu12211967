# MINI PROJECT(MAKE A MULTIPLE TYPE OBJECTIVE TYPE QUESTIONS/ANSWERS USING DICTIONARY )

def quiz(name):
#QUESTIONS FOR FIRST ROUND
q1="""q1.)Is Python case sensitive when dealing with Identifiers?
a.True
b.False
c.machine dependent
d.none of the mentioned """
q2="""q2.)Which one of these is floor division?
a./
b.//
c.%
d.None of the mentioned"""
q3="""q3.)What will be the output of following code
x=125
y=13
print(x//y)
a.9
b.10
c.8
d.9.62"""
q4="""q4.)What is the answer to this expression, 22 % 3 is?
a.7
b.1
c.0
d.5"""
q5="""q5.)"a"+"bc"=?
a.a
b.bcc
c.abc
d.bca"""
# QUESTIONS FOR SECOND ROUND
q6="""q1.)What will be the value of the following Python expression?
print(4**4)
a) 20
b) 256
c) 16
d) 8"""
q7="""q2.)Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom"""
q8="""q3.)Which of the following character is used to give single-line comments in Python?
a) //
b) #
c) !
d) /*"""
q9="""q4.)What is the order of precedence in python?
a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"""
q10="""q5.)What will be the output of the following Python code?
print(2*2+16/5-64)
a) -47.0
b) -57.0
c) 47.0
d) 57.0"""
# QUESTIONS FOR THIRD ROUND
q11="""q1.)Which of the following functions is a built-in function in python?
a) factorial()
b) print()
c) seed()
d) sqrt()"""
q12="""q2.)Which of the following is the use of id() function in python?
a) Every object doesn’t have a unique id
b) Id returns the identity of the object
c) All of the mentioned
d) None of the mentioned"""
q13="""q3.)Which of the following is not a core data type in Python programming?
a) Tuples
b) Lists
c) Class
d) Dictionary"""
q14="""q4.)26. What will be the output of the following Python expression if x=56.236?
print("%.2f"%x)
a) 56.236
b) 56.23
c) 56.0000
d) 56.24"""
q15="""q5.)What will be the output of the following Python function?
len(["hello",2, 4, 6])
a) Error
b) 6
c) 4
d) 3"""
# QUESTIONS FOR FOURTH ROUND
q16="""q1.)Which one of the following is not a keyword in Python language?
a) pass
b) eval
c) assert
d) nonlocal"""
q17="""q2.)What arithmetic operators cannot be used with strings in Python?
a) *
b) –
c) +
d) All of the mentioned"""
q18="""q3.)Which of the following statements is used to create an empty set in Python?
a) ( )
b) [ ]
c) { }
d) set()"""
q19="""q4.)What will be the output of the following Python expression?
round(4.576)
a) 4
b) 4.6
c) 5
d) 4.5"""
q20="""q5.)What is output of print(math.pow(3, 2))?
a) 9.0
b) None
c) 9
d) None of the mentioned"""
# QUESTIONS FOR FIFTH ROUND
q21="""q1.)Which of the following is a Python tuple?
a) {1, 2, 3}
b) {}
c) [1, 2, 3]
d) (1, 2, 3)"""
q22="""q2.)Python is a __________ level language?
a)high
b)low
c)middle
d)none of these"""
q23="""q3.)Which of the following types of loops are not supported in Python?
a)for
b)while
c)do-until
d)none of the above"""
q24="""q4.)What will be the output of the following code snippet?
example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
print(example[-3:-1])
a)["Monday","Tuesday"]
b)["Sunday","Monday"]
c)["Tuesday","Wednesday"]
d)["Wednesday","Monday"]"""
q25="""q5.)What will be the output of the following code snippet?
a = [1, 2]
print(a * 3)
a)error
b)[1,2]
c)[1,2,1,2]
d)[1,2,1,2,1,2]"""
round1={q1:"a",q2:"b",q3:"a",q4:"b",q5:"c"}
round2={q6:"b",q7:"c",q8:"b",q9:"d",q10:"b"}
round3={q11:"b",q12:"b",q13:"c",q14:"d",q15:"c"}
round4={q16:"b",q17:"b",q18:"d",q19:"c",q20:"a"}
round5={q21:"d",q22:"b",q23:"c",q24:"a",q25:"d"}
print("hello",name,",","Welcome to the quiz world")
print("Round 1(out of Round 5)")
score=0
total=0
# ROUND 1
for i in round1:
print(i)
ans=input("enter the answer: a/b/c/d")
if ans==round1[i]:
print("Congratulations,your Answer is correct")
score=score+1
total=total+1
else:
print("oops,your answer is wrong")
total=total+1
print("you have completed Round 1")
print("Round 2(out of Round 5)")
# ROUND 2
for i in round2:
print(i)
ans=input("enter the answer: a/b/c/d")
if ans==round2[i]:
print("Congratulations,your Answer is correct")
score=score+1
total=total+1
else:
print("oops,your answer is wrong")
total=total+1
print("you have completed Round 2")
print("Round 3(out of Round 5)")
# ROUND 3
for i in round3:
print(i)
ans=input("enter the answer: a/b/c/d")
if ans==round3[i]:
print("Congratulations,your Answer is correct")
score=score+1
total=total+1
else:
print("oops,your answer is wrong")
total=total+1
print("you have completed Round 3")
print("Round 4(out of Round 5)")
# ROUND 4
for i in round4:
print(i)
ans=input("enter the answer: a/b/c/d")
if ans==round4[i]:
print("Congratulations,your Answer is correct")
score=score+1
total=total+1
else:
print("oops,your answer is wrong")
total=total+1
print("you have completed Round 4")
print("Round 5(Final Round)")
# ROUND 5(FINAL ROUND)
for i in round5:
print(i)
ans=input("enter the answer: a/b/c/d")
if ans==round5[i]:
print("Congratulations,your Answer is correct")
score=score+1
total=total+1
else:
print("oops,your answer is wrong")
total=total+1
print("you have completed all the Rounds")
print("Final Score:",score,"/",total)
name=str(input("Enter your Name:"))
regi=int(input("Enter your Registration Number"))
roll=int(input("Enter your Roll Number"))
print("Are you ready for quiz")
answer=input("yes/no")
if answer=="yes":
quiz(name)
elif answer=="no":
print("Thanks for Joining")
else:
print("Wrong Input")
extra=input("Enter 1 to Restart the quiz or Enter 2 to Submit the quiz")
if extra=="1":
quiz(name)
elif extra=="2":
print("your quiz is Submitted Successfully")
else:
print("wrong input")
# EXECUTION OF THE CODE
Enter your Name:himanshu kumar
Enter your Registration Number12211967
Enter your Roll Number27
Are you ready for quiz
yes/noyes
hello himanshu kumar , Welcome to the quiz world
Round 1(out of Round 5)
q1.)Is Python case sensitive when dealing with Identifiers?
a.True
b.False
c.machine dependent
d.none of the mentioned
enter the answer: a/b/c/da
Congratulations,your Answer is correct
q2.)Which one of these is floor division?
a./
b.//
c.%
d.None of the mentioned
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q3.)What will be the output of following code
x=125
y=13
print(x//y)
a.9
b.10
c.8
d.9.62
enter the answer: a/b/c/da
Congratulations,your Answer is correct
q4.)What is the answer to this expression, 22 % 3 is?
a.7
b.1
c.0
d.5
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q5.)"a"+"bc"=?
a.a
b.bcc
c.abc
d.bca
enter the answer: a/b/c/dc
Congratulations,your Answer is correct
you have completed Round 1
Round 2(out of Round 5)
q1.)What will be the value of the following Python expression?
print(4**4)
a) 20
b) 256
c) 16
d) 8
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q2.)Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom
enter the answer: a/b/c/dc
Congratulations,your Answer is correct
q3.)Which of the following character is used to give single-line comments in Python?
a) //
b) #
c) !
d) /*
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q4.)What is the order of precedence in python?
a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction
enter the answer: a/b/c/dd
Congratulations,your Answer is correct
q5.)What will be the output of the following Python code?
print(2*2+16/5-64)
a) -47.0
b) -57.0
c) 47.0
d) 57.0
enter the answer: a/b/c/db
Congratulations,your Answer is correct
you have completed Round 2
Round 3(out of Round 5)
q1.)Which of the following functions is a built-in function in python?
a) factorial()
b) print()
c) seed()
d) sqrt()
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q2.)Which of the following is the use of id() function in python?
a) Every object doesn’t have a unique id
b) Id returns the identity of the object
c) All of the mentioned
d) None of the mentioned
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q3.)Which of the following is not a core data type in Python programming?
a) Tuples
b) Lists
c) Class
d) Dictionary
enter the answer: a/b/c/dc
Congratulations,your Answer is correct
q4.)26. What will be the output of the following Python expression if x=56.236?
print("%.2f"%x)
a) 56.236
b) 56.23
c) 56.0000
d) 56.24
enter the answer: a/b/c/dd
Congratulations,your Answer is correct
q5.)What will be the output of the following Python function?
len(["hello",2, 4, 6])
a) Error
b) 6
c) 4
d) 3
enter the answer: a/b/c/dc
Congratulations,your Answer is correct
you have completed Round 3
Round 4(out of Round 5)
q1.)Which one of the following is not a keyword in Python language?
a) pass
b) eval
c) assert
d) nonlocal
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q2.)What arithmetic operators cannot be used with strings in Python?
a) *
b) –
c) +
d) All of the mentioned
enter the answer: a/b/c/db
Congratulations,your Answer is correct
q3.)Which of the following statements is used to create an empty set in Python?
a) ( )
b) [ ]
c) { }
d) set()
enter the answer: a/b/c/dd
Congratulations,your Answer is correct
q4.)What will be the output of the following Python expression?
round(4.576)
a) 4
b) 4.6
c) 5
d) 4.5
enter the answer: a/b/c/dc
Congratulations,your Answer is correct
q5.)What is output of print(math.pow(3, 2))?
a) 9.0
b) None
c) 9
d) None of the mentioned
enter the answer: a/b/c/da
Congratulations,your Answer is correct
you have completed Round 4
Round 5(Final Round)
q1.)Which of the following is a Python tuple?
a) {1, 2, 3}
b) {}
c) [1, 2, 3]
d) (1, 2, 3)
enter the answer: a/b/c/dd
Congratulations,your Answer is correct
q2.)Python is a __________ level language?
a)high
b)low
c)middle
d)none of these
enter the answer: a/b/c/dd
oops,your answer is wrong
q3.)Which of the following types of loops are not supported in Python?
a)for
b)while
c)do-until
d)none of the above
enter the answer: a/b/c/dc
Congratulations,your Answer is correct
q4.)What will be the output of the following code snippet?
example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
print(example[-3:-1])
a)["Monday","Tuesday"]
b)["Sunday","Monday"]
c)["Tuesday","Wednesday"]
d)["Wednesday","Monday"]
enter the answer: a/b/c/da
Congratulations,your Answer is correct
q5.)What will be the output of the following code snippet?
a = [1, 2]
print(a * 3)
a)error
b)[1,2]
c)[1,2,1,2]
d)[1,2,1,2,1,2]
enter the answer: a/b/c/dd
Congratulations,your Answer is correct
you have completed all the Rounds
Final Score: 24 / 25
Enter 1 to Restart the quiz or Enter 2 to Submit the quiz
