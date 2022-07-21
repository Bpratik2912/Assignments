from questions.fibonacci import fibonacci_number
from questions.primenumber import prime_number
from questions.armstrong import armstrong_number
import time

def time_wrap(fn):
        """method to perform execution time!!!"""
        start_time = time.time()
        result= fn()
        print(result)
        end_time = time.time()
        print("total execution time:",end_time- start_time)

@time_wrap
def main_func():
    print("numbers for methods")
    print("1) fibonacci number\n2) prime number\n3) armstrong number")
    a = int(input("enter method number:"))

    if a == 1:
        return fibonacci_number.run(a)
    elif a==2:
        return prime_number.run(a)
    elif a==3:
        return armstrong_number.run(a)
    else:
        return " "
