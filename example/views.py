import ast
from django.shortcuts import render
from django.http import JsonResponse

# Example function to calculate time complexity
def calculate_time_complexity(code):
    """
    This is a basic parser to check code patterns and return 
    the corresponding time complexity. This logic can be improved.
    """
    try:
        # Parse the code using ast
        parsed_code = ast.parse(code)
        
        # Basic time complexity detection logic (can be extended)
        if any(isinstance(node, ast.For) for node in ast.walk(parsed_code)):
            return "O(n)"
        elif any(isinstance(node, ast.While) for node in ast.walk(parsed_code)):
            return "O(n)"
        elif any(isinstance(node, ast.If) for node in ast.walk(parsed_code)):
            return "O(1)"
        else:
            return "O(1)"  # Default case for simplicity

    except Exception as e:
        return str(e)


def time_complexity_view(request):
    """
    View to handle the form submission, input the code, and return the time complexity.
    """
    if request.method == 'POST':
        input_code = request.POST.get('code')
        complexity = calculate_time_complexity(input_code)
        return JsonResponse({'complexity': complexity})
    return render(request, 'index.html')
