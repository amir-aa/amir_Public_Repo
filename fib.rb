def fibonacci(n)
  if n < 2
    return n
  else
    return fibonacci(n-1) + fibonacci(n-2)
  end
end

# print first 10 Fibonacci numbers
for i in 0..9
  puts fibonacci(i)
end
