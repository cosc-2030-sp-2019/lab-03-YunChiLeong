# Yun Chi Leong
# COSC 2030-01
# 4 March 2019 
import operator
ops = {
       '+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow
       }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def operation(oper, val1, val2):
    if oper == '+':
        return val1+val2
    elif oper == '-':
        return val1-val2
    elif oper == '*':
        return val1*val2
    else:
        if val2 == 0:
            return None
        else:
            return val1/val2
    
def calculate(exp):
    stack = []
    result = 0
    for i in exp:
        # if operator, push into stack
        if i == operator:
            stack.push(i)
        else:
        # else number, pop 2 elemets off the stack 
            print('stack: ', stack, 'where i = ', i)
            operand2 = stack.pop(0)
            operand1 = stack.pop(1)
            # call operation function
            result = operation(ops[i], operand1, operand2)
            if result is None:
                print("Cannot divide by zero")
                exit(-1)
            else:
                stack.push(result)
    return result

print ("Start of Polish Notation Evaluator")
exp_file = open("Expressions1.txt", 'r')
for line in exp_file:
        exp_file = line.rstrip().split(' ')
        answer = calculate(exp_file)
        print('RESULT: %f' % answer)
print ("End of Polish Notation Evaluator")
