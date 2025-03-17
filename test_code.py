"""
Test file for eco-code-analyzer with various code patterns.
"""

# Inefficient loop (could be a list comprehension)
def inefficient_loop():
    result = []
    for i in range(100):
        result.append(i * 2)
    return result

# Efficient list comprehension
def efficient_list_comp():
    return [i * 2 for i in range(100)]

# Inefficient string concatenation
def inefficient_string_concat(items):
    result = ""
    for item in items:
        result += str(item)  # Inefficient string concatenation
    return result

# Efficient string joining
def efficient_string_join(items):
    return ''.join(str(item) for item in items)

# Inefficient resource management
def inefficient_file_handling(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content

# Efficient resource management with context manager
def efficient_file_handling(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content

# Inefficient nested loops (O(n²) complexity)
def inefficient_nested_loops(items):
    result = []
    for i in items:
        for j in items:
            result.append(i * j)
    return result

# More efficient approach using list comprehension
def efficient_algorithm(items):
    return [i * j for i in items for j in items]

# Inefficient dictionary lookup with exception handling
def inefficient_dict_lookup(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

# Efficient dictionary lookup with get method
def efficient_dict_lookup(dictionary, key, default=None):
    return dictionary.get(key, default)

# Inefficient repeated file operations in a loop
def inefficient_file_operations(filenames):
    results = []
    for filename in filenames:
        with open(filename, 'r') as f:
            results.append(f.read())
    return results

# Efficient file operations (reading once)
def efficient_file_operations(filename, indices):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [lines[i] for i in indices if i < len(lines)]

# Inefficient recursive function without memoization
def inefficient_fibonacci(n):
    if n <= 1:
        return n
    return inefficient_fibonacci(n-1) + inefficient_fibonacci(n-2)

# Efficient recursive function with memoization
memo = {}
def efficient_fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = efficient_fibonacci(n-1) + efficient_fibonacci(n-2)
    return memo[n]

if __name__ == "__main__":
    print(inefficient_loop())
    print(efficient_list_comp())
