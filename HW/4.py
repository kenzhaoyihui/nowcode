import sys

def split_8(s):
    num8 = len(s)/8
    if num8<1:
        print s+'0'*(8-len(s))
    else:
        for i in range(num8):
            print s[8*i:8*(i+1)]
        a = s[-(len(s)%8):]
        print a+'0'*(8-len(a))


a = raw_input()
b = raw_input()
split_8(a)
split_8(b)
    

# while True:
#     try:
#         def split_8(s):
#             k=len(s)/8
#             for i in range(k):
#                 print s[i*8:(i+1)*8]
#             if len(s)%8>0:
#                 print s[-(len(s)%8):].ljust(8,'0')
#         a=raw_input()
#         b=raw_input()
#         split_8(a)
#         split_8(b)
#     except:
#         break