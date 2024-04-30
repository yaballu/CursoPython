linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort())

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(reverse=True))

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(key=lambda x: len(x)))

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(key=lambda x: len(x), reverse=True))