list=['Wake up early','breakfast','jogging','bathing']
print("To do list")
for index,char in enumerate (list,start=1):
    print(f"{index}.{char}")
def add_to_list(text1):
    list.extend(text1)
    print(list)
text=input("enter a to do list :")
text1=text.split()
for char in text1:
    if char=="add":
        text1.remove("add")
        add_to_list(text1)
