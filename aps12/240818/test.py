x = [(1, 0)]
stt = x[0][0]
end = x[-1][0]
mid = (stt + end) // 2
x_f = x[stt:mid]
x_b = x[mid:end]
print(x_f,x_b)