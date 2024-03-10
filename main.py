import sys
list=['Wake up early','breakfast','jogging','bathing']
print("To do list")
for index,char in enumerate (list,start=1):
    print(f"{index}.{char}")
def add_to_list(text1):
    list.extend(text1)
    for index,char in enumerate(list,start=1):
        print(f"{index}.{char}")
def switch(op):
        if op=="1":
            text=input("enter a to do list :")
            text1=text.split()
            for char in text1:
                if char=="add":
                    text1.remove("add")
                    add_to_list(text1)
                    print(f"new task is added ")
        elif op=="2":
            completed=input("enter here :")
            for char in list:
                if char ==completed:
                    list.remove(completed)
                    print(f"The completed {completed} task is removed")
            for index,char in enumerate (list,start=1):
                print(f"{index}.{char}")
        elif op=="3":
            sys.exit(3)
        else:
            return "invalid option enter 1 10 3"
while True:
    print(f"choose any option given below\n1.enter to add to the to do list\n2.enter an complted task\n3.exit\n")
    op=input("enter:")

    switch(op)
    if op=="3":
        break

