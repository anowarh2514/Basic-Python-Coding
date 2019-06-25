def divide(a,b):
      try:
           return a/b
      except ZeroDivisionError:
          return "Divide by Zero is meaningless !"

print(divide(1,0))
print(" ----End of the program ----")