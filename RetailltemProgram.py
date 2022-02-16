import RetailltemClass as r 

des1 = "Jacket"
des2 = "Designer Jeans"
des3 = "Shirt"

inv1 = "12"
inv2 = "40"
inv3 = "20"

p1 = "59.95"
p2 = "34.95"
p3 = "24.95"

item1 = r.Retailltem(des1,inv1,p1)
item2 = r.Retailltem(des2,inv2,p2)
item3 = r.Retailltem(des3,inv3,p3)

print("NO. \t Description \t Units \t Price ")
print("Item1\t",item1.get_description(),"\t",item1.get_inventory(),"\t",item1.get__price())
print("Item2\t",item2.get_description(),"",item2.get_inventory(),"\t",item2.get__price())
print("Item3\t",item3.get_description(),"\t\t",item3.get_inventory(),"\t",item3.get__price())
