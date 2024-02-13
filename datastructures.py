my_list = ["one day", "Hamilton", "will be mine"]
my_list.append("Charles Leclerc")

print(my_list)
print(my_list[0])
my_list[1]="Charles " #mutable
print(my_list[1],"races for Mercedes in f1")
print(f"{my_list[1]} races for Mercedes in f1")


thislist = ["Hamilton","Charles Leclerc","Daniel Riccardo"]
thislist.insert(2, "Carlos Sainz")
print(thislist)


# tuple datastructures immutable cannot change values
my_tuple = ("Mercedes","Ferrari", "McLaren","Williams")
print(my_tuple)
# my_tuple[1]="Hamilton"
print(f"{my_tuple[1]} races for Ferrari in F1")


# set datastructures
my_set={"Abu Dhabi", "Hamilton", "Leclerc", "Daniel Riccardo"}
print(my_set)


# dictionary datastructures
my_dict={"name":"Lewis Hamilton","Age": "recently adult", "Gender":"Male","Team":"Mercedes"}
print(my_dict)
print(my_dict["Age"])
print(my_dict["Gender"])
print(my_dict["name"])
print(my_dict["name"])