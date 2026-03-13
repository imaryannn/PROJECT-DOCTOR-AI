def analyze_code(code):

    suggestions = []

    if "while(True)" in code:
        suggestions.append("Infinite loop detected. Check loop condition.")

    if "print(" in code:
        suggestions.append("Too many print statements. Consider using logging.")

    if "==" in code:
        suggestions.append("Make sure comparison operators are used correctly.")

    if len(code) < 50:
        suggestions.append("Code is very small. Try adding more functionality.")

    if not suggestions:
        suggestions.append("Code looks good. No major issues detected.")

    return suggestions
