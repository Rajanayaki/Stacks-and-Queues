minelement=0
def createstack():
  stack=[]
  return stack
def push(stack,data):
  global minelement
  if isEmpty(stack)==True and minelement==0:
    minelement=data
    stack.append(data)
  else:
    if data<minelement:
      minelement=data
      stack.append(data)
def top(stack):
  if len(stack)<1:
    print("Stack empty")
  else:
    return stack[-1]
def pop(stack):
  if len(stack)<1:
    print("stack underflow")
  else:
    stack.pop()
def isEmpty(stack):
  if len(stack)<1:
    return True
  else:
    return False
def printstack(stack):
  print(*stack)
def sort(stack):
  minelement=0
  while(isEmpty(stack)!=True):
    if minelement > top(stack):
      minelement=top(stack)
      pop(stack)
  return minelement
s=createstack()
stacklist=list(map(int,input("Enter the stack elements: ").split()))
for i in range(len(stacklist)):
  push(s,stacklist[i])
print(minelement)
