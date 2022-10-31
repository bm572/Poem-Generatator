# #poem generator

#imports the library time to use time.sleep in our program
import time
#Get input from our user and store as a variable
place= input("Type in a place. ")
tree= input("Type in a type of tree. ")
verb= input("Type in a verb. ")
person = input("Type in your favorite person ")
food = input("Type in your favorite food. ")

#Adds a few spaces before our poem prints
print("\n\n")

#waits one second before printing the next line
time.sleep(1) 

#prints poem
print("I want to sit by the bank of the " +place+ "," + " with " + food)
time.sleep(1) 

print("\tin the shade of the " +tree + " tree,")
time.sleep(1) 

print("And " +verb+ " with " + person + ",")
time.sleep(1) 

print("\t\t and wait for whatever " + "and, whoever that’s waiting for me.")