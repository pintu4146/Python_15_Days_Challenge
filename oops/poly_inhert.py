# class Vehicle:
#     def __init__(self, brand: str) -> None:
#         self.brand = brand
#
#
#     def start(self):
#         return f'vehicle name: {self.brand}'
#     def stop(self):
#         return f'vehicle stop: {self.brand}'
#
# class Car(Vehicle):
#     def __init__(self, car_name: str):
#         super().__init__(car_name)
#         self.car_name = car_name
#
#     # def start(self):
#     #     return "Car started"
#
#
#
# car_honda = Car("Honda")
#
# print(car_honda.start())
# # print()

"""
Input = "$84,123"
output = "$32,148"
"""

def reverse_only_num(intput: str):
    i , j = 0 , len(intput)-1

    while i < j :
        # 84, 123
        if int(intput[i]).isdigit() and int(intput[j]).isdigit():
            intput[i] , intput[j] = intput[j], intput[i]
            i += 1
            j -= 1
        elif intput[i].isdigit() == False:
            i += 1
        else:
            j -= 1
    return intput

In = "$84,123"
print(reverse_only_num(intput=In))




