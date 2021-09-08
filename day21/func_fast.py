# function 폴더(외부)에서 정의한 함수를 호출하여 사용

from function.square import square
from function.extends_var import merge_text, calc_avg

print(merge_text('a '))
print(merge_text('a ', 'b '))

print(square(5))
print(square(6))

