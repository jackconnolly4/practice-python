# conditional deliberate practice page #2 is STILL broken on Actualize website, so this is actually the 3rd condtional delib practice set

# Write a program that stores a customer's age and a movie's time in two separate variables. Then calculate the price of a movie ticket based on the following conditions:

# If the age is 12 years old or younger, the ticket price is $5.
# If the age is between 13 and 59 years old and the movie is before 6 PM, the ticket price is $7. After 6 PM, the ticket price is $10.
# If the customer is 60 years old or older, the ticket price is $7.

# age = 55
# time = 8

# if age <+ 12:
#   price = 5
# elif age > 60:
#   price = 7
# elif time < 6: 
#   price = 7
# else:
#   price = 10

# print(price)

# alt: 

# if age <= 12:
#     ticket_price = 5
# elif age >= 13 and age <= 59:
#     if time < 18:
#         ticket_price = 7
#     else:
#         ticket_price = 10
# elif age >= 60:
#     ticket_price = 7

# print("Ticket price: $" + str(ticket_price))

# Write a program to store the type of book (regular, reference, or special collection) and the number of days its overdue. Then calculate the fine amount based on the following conditions:

# If the book is a regular book and overdue by up to 7 days, the fine is $1 per day.
# If the book is a regular book and overdue by more than 7 days, the fine is $2 per day.
# If the book is a reference book, there is no fine, regardless of the number of days overdue.
# If the book is a special collection book, the fine is $5 per day, regardless of the number of days overdue.