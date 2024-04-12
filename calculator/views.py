from django.shortcuts import render
from .static.models import Calculation

def calculator_view(request):
    if request.method == 'POST':

        calc_chars = request.POST.get('calc_chars')

        elements = separate_chars(calc_chars)
        print(elements)

        # Calculate the result
        result = calculate_result(elements)
        
        Calculation(expression=calc_chars, result=result).save()
        
        result = round(result, 2)
        calc_chars = str(result)
        return render(request, 'calculator.html', {'calc_chars': calc_chars})
    else:
        return render(request, 'calculator.html')
    
    
def separate_chars(calc_chars):
    # Separate the characters based on the operator
    operators = ['+', '-', '*', '/']
    current_chars = ''
    separated_chars = []
    for char in calc_chars:
        if char in operators:
            separated_chars.append(current_chars)
            separated_chars.append(char)
            current_chars = ''
        else:
            current_chars += char
    separated_chars.append(current_chars)
    return separated_chars

def calculate_result(elements):
    # Calculate the result
    result = None
    current_operator = None
    for element in elements:
        if result is None:
            if is_float(element):
                result = float(element)
                continue
            else:
                continue
        
        if is_float(element):
            result = do_math(result, float(element), current_operator)
        elif element == '+':
            current_operator= element
        elif element == '-':
            current_operator= element
        elif element == '*':
            current_operator= element
        elif element == '/':
            current_operator= element
        print(result, element)
            
    return result

def do_math(float1, float2, operator):
    if operator == '+':
        return float1 + float2
    elif operator == '-':
        return float1 - float2
    elif operator == '*':
        return float1 * float2
    elif operator == '/':
        return float1 / float2
    else:
        return None       
    
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

