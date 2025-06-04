mock_questions = [
    {
        "question": "What is the difference between a list and a tuple in Python?",
        "answer": "The main difference is that lists are mutable, meaning you can change, add, or remove elements after the list is created. Tuples, on the other hand, are immutable — once defined, their contents can’t be altered. This makes tuples faster and more memory-efficient, and they’re often used for fixed collections of items.",
    },
    {
        "question": "Can you explain what a Python dictionary is?",
        "answer": "A dictionary in Python is a collection of key-value pairs. It’s similar to a real-world dictionary where you look up a word (the key) and get its definition (the value). Dictionaries are unordered and mutable, and they allow for fast lookups based on unique keys.",
    },
    {
        "question": "What is the purpose of the 'self' keyword in Python classes?",
        "answer": "'self' refers to the instance of the class and is used to access variables and methods that belong to that instance. It allows each object to maintain its own state and behavior. Think of it as a way for the object to refer to itself while executing its methods.",
    },
    {
        "question": "How does Python handle memory management?",
        "answer": "Python handles memory management through a built-in garbage collector that automatically tracks and frees up memory that's no longer in use. It uses reference counting and a cyclic garbage collector to manage objects efficiently behind the scenes, so developers usually don't need to manage memory manually.",
    },
    {
        "question": "What are Python list comprehensions and why are they useful?",
        "answer": "List comprehensions provide a concise way to create lists in Python. Instead of writing multiple lines with loops, you can generate lists in a single readable line. They’re not just shorter — they’re often faster and more elegant, especially when working with transformations or filters.",
    },
    {
        "question": "What does the 'with' statement do in Python?",
        "answer": "The 'with' statement is used to wrap the execution of a block with methods defined by a context manager. It’s commonly used for managing resources like files. When you open a file using 'with', Python makes sure it’s properly closed, even if an error occurs inside the block.",
    },
    {
        "question": "Why is Python considered an interpreted language?",
        "answer": "Python is considered an interpreted language because its code is executed line by line by an interpreter at runtime, rather than being compiled into machine-level instructions beforehand. This makes Python more flexible and easier to debug, but sometimes a bit slower than compiled languages.",
    },
    {
        "question": "What is a lambda function in Python?",
        "answer": "A lambda function is a small, anonymous function defined using the 'lambda' keyword. It can take any number of arguments but only one expression. It's often used for quick operations where defining a full function would be overkill — for example, sorting a list by custom criteria.",
    },
    {
        "question": "What is the difference between 'is' and '==' in Python?",
        "answer": "'==' checks if two variables have the same value, while 'is' checks if they reference the same object in memory. So two different objects can be 'equal' in value but still be different instances, and that’s where 'is' and '==' give different results.",
    },
    {
        "question": "How does exception handling work in Python?",
        "answer": "Python uses try-except blocks for exception handling. When an error occurs in the try block, Python jumps to the except block to handle it gracefully without crashing the program. You can also use 'finally' to execute code regardless of whether an exception occurred or not.",
    },
]
