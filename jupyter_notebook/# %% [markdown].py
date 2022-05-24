# %% [markdown]
# # Python ka chilla with baba aamar
# ## How to use jupyter notebook
# ### Basics of python
# **01- My first programme**
# 

# %%

print(2+3)
print("hello world on output")
print("we are learning python with aamar")

# %% [markdown]
# **02- operators**

# %%
print(2+3)
print(4-1)
print(3*4)
print(9/3)
print(13%2)
print(9//3)
print(3**2)

print(3**4/3*4/3+5-4)



# %% [markdown]
#  **pemadas
#  parenthesis, exponent,multiplication, divide, addition, subtraction
#  it work left to right M D and A S **

# %% [markdown]
# **03- strings**

# %%
print("Hello world on output")
print("we are learning python with aamar  ")

print('test for single quote')
print("Test for double quote")
print(''' test for triple quote''')

print("what's up   ?")
print("i am wasim anjum")

# agr python interpretor nhi a raha to ctrl+shift+p press karay or select interpreter choose karary

# %% [markdown]
# **04- comments**

# %%
print(" hello world on output")  #press left ctrl +/ to comment out 
print("we are learning python with aamar") # print a string
print(2+3) # print opeartor functions wwith numbers


# %% [markdown]
# **05- variables**

# %%
# # variables: objects containing specific values
# from tkinter import Variable


x=5
print(x)
y="we are learning python with aamar"
print(y)
X=15
print(X) # upto down write ho ga
x=x+10


# # types of variables or class of variables
type(x)
print(type(x))
type(y)
print(type(y))

# Rules to assign a Variable
#1 the variable should contain letter, nuumber or underscore in python
# 2 do not start with number mean 2y
# 3 spaces are not allowed
# 4 do not use keyword in python function (break, mean,, median, test etc)
# 5 variable name is shot and descriptive 
# 6 variable is case sensitive (lowercase upper case letters) use lowercase letter is best

fruit_basket= 8
# del fruit_basket ye vala function karnay peeshla variable delet ho jy ga or terminal ma show ni ho ga


fruit_basket="mangoes"

print(fruit_basket)
print(type(fruit_basket))


# %% [markdown]
# **06- input_variables**

# %%
fruit_basket="mangoes"
print(fruit_basket)

#  input fuction 
fruit_basket=input("what is your favourite fruit  ?")
print(fruit_basket)

# input function of 2nd stage variable
name=input("what is your name  ?")
greetings="hello"
print(greetings, name)

#  another way of stage 2 input function 
name=input("what is your name  ?")
print("hello", name)

#  3RD STAGE OF INPUT FUNCTION 
name=input("what is your name  ?")
age=input("how old are you  ?")
greetings="hello"
print(greetings,name,"you are still young")

# %% [markdown]
# **07- conditional logics**

# %%
#  logical operator are true or false, yes or no, 0 or 1
# equal to              ==
# not equal to          !=
# less than             <
# greater than           >
# less than and equal to <=
# greater than and eual to >=




# #  4 equal to 4
print(4==4)  
print(4!=4)
# #  logical opeartors
print(4<5)
print(4>5)
print(4<=5)
print(6>=4)

# #  application of logical operators
# #  hammad na schol jana hai us ki age 4 sall hai lakin school valay khty kk vo 5 saal vala bacha la ga 
hammad_age=4
age_at_school=5
print(hammad_age==age_at_school)


#  input function and logical operators
age_at_school=5
hammad_age=input("how old is hammad    ?") # input function

hammad_age=int(hammad_age)
print(type(hammad_age))
print(hammad_age==age_at_school)   #logical operator



# %% [markdown]
# **08- types of conversion**

# %%
x=10
y=10.2
z="hello"  #string
print(type(x))
print(type(y))
print(type(z))
x=x*y
print(type(x))

# # implicit type conversion
x=x+y
print(x,"type of x :", type(x))

# explicit type conversion
age= input("what is your age  ?")
print(type(age))   # yaha pr age ki class string a re hai  lakin age ki type int ani chahye is liy neechay phr new likha hai
# # or 
age=input("what is your age   ?")
age=int(age)
print(type(age))
# # or
age=input("what is your age    ?")
print(age, type(int(age)))

#  flaot k liay
age=input('what is your age  ?')
print(age,type(float(age)))
#  to convert into string
print(age,type(str(age)))

# name
name=input("what is your name   ?")
print(name,type(str(name)))

# %% [markdown]
# **09- if else elif**

# %%
required_age_at_school=5
hammad_age=4
if hammad_age==required_age_at_school:
    print("hammad can join the school") #terminal ma kush ni print ho ra ku k hamad ki age km hai 
required_age_at_school=5
hammad_age=9
if hammad_age==required_age_at_school:
    print("hammad can join the school")
elif hammad_age > required_age_at_school:
    print("hammad can join the higher secondary school")
elif hammad_age <=2:
    print("you should take care of your baby")

else:
    print("hammad cannot go to school")


# %% [markdown]
# **10- functions**

# %%
print("we aress learning with aamar")
print("we are learning with aamar")
print("we are learning with aamar")
print("we are learning with aamar")

#defining a function
#no 1
def print_codanics():
    print("we are learning python with aamar")
    print("we are learning python with aamar")
    print("we are learning python with aamar")
print_codanics()

#2 
def print_codanics():
    text= "we are learning python with aamar"
    print(text)
    print(text)
    print(text)
print_codanics()
# iskka ye faida hai k hm variabl ma change kray ga vo sb line ma change ho jy ga

# 3
def print_codanics(text):
    print(text)
    print(text)
    print(text)
print_codanics("we are learning python  bbb  with aamar")


# 4 defining a function with if, elif and else statement
def school_calculator(age, text):
    if age == 5:
        print("hammad can join the school")
    elif age > 5: 
        print("hammad can join the higher seconadary school")
    else:
        print("hammad is still a baby")
school_calculator(2, "wasim" )   # yaha hm age ko change kry to fifferernt ans ay gay   


# agr hm function ma hammad name khtm kr day to kush nhi terminal ma ay ga isk liay hm ko degf valaly function ma sa text khtm krna ho ga phr print ho ga 

# defining a future function
def future_age(age):
    new_age=age+20
    return new_age
future_predicted_age= future_age(18)
print(future_predicted_age)





# %% [markdown]
# **11- loops**

# %%
# two types while loops and for loops
# while loops ma hm koi bhi cheez define kr saktay hai

#while loops
x=0
while(x<5):
    print(x)
    x=x+1 

# for loops
for x in range (5,10):
    print(x)

#array, it mean dat set
days= ["monday", "tuesday","wednesday","thursday","friday","saturday", "sunday"]
for d in days:
    print(d)
# or agr hm na koi loop break krni hai
days= ["monday", "tuesday","wednesday","thursday","friday","saturday", "sunday"]
for d in days:
    if (d=="friday"):break
    print(d)
#  or 
days= ["monday", "tuesday","wednesday","thursday","friday","saturday", "sunday"]
for d in days:
    if (d=="friday"):continue  # in this function freday is skipped
    print(d)



# %% [markdown]
# **12- import libraries**

# %%
# # if you want to print the value of pi 
import math
print("The value of pi is", math.pi)

# statistics
import statistics
x=[150, 250, 350, 450]
print(statistics.mean (x))
#statistics. # bht saray function open ho jy ga stat k 

#imp libraries
#numpy, pandas

# %% [markdown]
# **13- trouble shooting**

# %%
print("we are learning python with aamar")  # yha agr hm qqqquotation na da to syntax error ata hai

print(25/0)  # runtime error math ma ata hai

name="aamar"
print("hello", name)
# agr hm comma ki jga +lga da to space khtm ho jy gi
name="aamar"
print("hello"+ name)


# %%
# how to install libarries in vsc jupyter
pip install seaborn

# %%
pip install seaborn


