'''Did for my own understanding, Wasn't able to directly write it in lamda function'''


# def accounting_routine(l):
#     total_result = []
#     for order in l:
#         order_number = order[0]
#         quantity = order[2]
#         price_per_item = order[3]

#         total_value = quantity * price_per_item

#         if total_value < 100:
#             total_value += 10
#         total_result.append(order_number, total_value)
#     return total_result

# order_values = accounting_routine(orders)
# print(order_values)


orders = [
    [34587, "Learning Python", 4, 40.95],
    [98762, "Programming Python", 5, 56.80],
    [77226, "Head First Python", 3, 32.95],
    [88112, "Einführung in Python3", 3, 24.99]
]

a = list(map(lambda x: (x[0], x[2] * x[3] +(10 if x[2] * x[3] <100 else 0)),orders))
print(a)