employees ={"jack":100000,
            "Tom":50000,
            "Roy":120000,
            "eve":10000
}
# with noraml way
# top_earner=[]
# for key,val in employees.items():
#     if val>=100000:
#         top_earner.append((key,val))
#
# print(top_earner)


#with  List Comprehension
top_earner  = [(k,v) for k,v in employees.items() if v>=100000]
print(top_earner)
# top_earners = [(k, v) for k, v in employees.items() if v >= 100000]