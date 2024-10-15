from langchain_experimental.utilities import PythonREPL

python_repl = PythonREPL()

result = python_repl.run("print('ola')")
print(result)
