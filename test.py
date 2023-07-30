from html_parser import html_to_context
from pdf_parser import pdf_to_context


c = html_to_context()

print(len(c))

t = 0
for con in c:
    t+=len(con)
    print(len(con))

avg1 = t/len(c)

c = pdf_to_context()
t = 0
for con in c:
    t+=len(con)
    print(len(con))

avg2 = t/len(c)

print(len(c))
print(avg1, avg2)