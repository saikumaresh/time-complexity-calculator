import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from django.http import HttpResponse

# Time Complexity Analyzer placeholder (you need to implement the actual logic here)
class TimeComplexityAnalyzer:
    def analyze(self, code_input):
        # Dummy complexity analysis logic
        # Replace this with actual time complexity detection code
        if "for" in code_input and "while" in code_input:
            return "O(n^2)"
        elif "for" in code_input:
            return "O(n)"
        else:
            return "O(1)"

# Function to plot the complexity graph
def plot_complexity_graph(complexity):
    complexities = {
        'O(1)': [1] * 10,
        'O(n)': list(range(1, 11)),
        'O(n log n)': [x * (x ** 0.5) for x in range(1, 11)],
        'O(n^2)': [x ** 2 for x in range(1, 11)],
        'O(2^n)': [2 ** x for x in range(1, 11)],
        'O(n!)': [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880],
    }

    # Create the plot
    plt.figure(figsize=(6, 4))
    n_values = list(range(1, 11))  # Input size range (n = 1 to 10)
    plt.plot(n_values, complexities[complexity], label=complexity, marker='o')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Operations")
    plt.title(f"Growth of {complexity}")
    plt.grid(True)
    plt.legend()

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    # Encode the plot image in base64 to embed it in HTML
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return image_base64

# Main view function to analyze code and display results
def analyze_code(request):
    if request.method == 'POST':
        code_input = request.POST.get('code_input')  # Get the input Python code from the form

        # Analyze the time complexity of the code
        analyzer = TimeComplexityAnalyzer()
        complexity = analyzer.analyze(code_input)

        # Generate the graph based on the complexity
        graph = plot_complexity_graph(complexity)

        # Render the result page with complexity and graph
        return render(request, 'result.html', {'complexity': complexity, 'graph': graph})

    # If the request is a GET request, render the input form page
    return render(request, 'index.html')
