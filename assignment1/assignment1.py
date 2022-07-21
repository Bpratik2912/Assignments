s = input("enter camel string to convert snake string:")
d = input("enter snake string to convert camel string:")
def camtosnake(s):
    pattern = [char for char in s if char.isupper()]
    
    p=str(pattern)
    print(p,pattern)
    res = ""
    for i in s:
        if i in p:
            i=i.lower()
            res= res + "_" + i
        else:
            res = res + i
    return res

print(camtosnake(s))

def snaketocam(d):
    temp = d.split('_')
    print(temp)
    final = temp[0] + ''.join(ele.title() for ele in temp[1:])
    k= str(final)
    return k 

print(snaketocam(d))

# import string
# s= "helloIAmPratikBariya"
# def camtosnake(s):
#     pattern = [string.ascii_uppercase]
#     print(pattern)
#     p=str(pattern)
# #     # print(p,pattern)
#     res = ""
#     for i in s:
#         if i in p:
#             i=i.lower()
#             res= res + "_" + i
#         else:
#             res = res + i
#     return res

# print(camtosnake(s))