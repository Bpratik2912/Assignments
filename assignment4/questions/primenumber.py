import time
from base import assignment
# from main import time_wrap
class prime_number(assignment):
    # @time_wrap
    def run(self):
        """to find prime number: number should be divisible by only 1 and itself."""
        a = int(input("enter a number to find primenumber:"))
        # time.sleep(5)
        if (a>1):
            for i in range(2,a):
                # print(i)
                if a%i==0:
                    return 'it is NOT a prime number.'
                    break
            else:
                    return 'it is a prime number'
        else:
            return 'it is NOT a prime number'

# print(prime_number.run(a))