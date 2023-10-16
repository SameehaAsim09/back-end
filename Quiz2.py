def skip_elements(elements):
    ans = [element for i , element in enumerate(elements) if i%2 == 0 ]
    return ans

print(skip_elements(['a','b','c','d','e','f','g']))
print(skip_elements(['apple','banana','carrot','dates','grapes']))
