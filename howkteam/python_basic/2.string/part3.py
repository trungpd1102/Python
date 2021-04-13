# a = 'My name is %s, now I\'m %d years old'

# result = a %('Trung', 26)

# ----------------------------------------------------
# class SomeThing:  
#     def __repr__(self):
#         return 'Đây là __repr__'
#     def __str__(self):
#         return 'Đây là __str__'

# thing = SomeThing() # thing là một đối tượng trong class SomeThing

# # print(type(thing))
# # print(thing)

# print('%r' %(thing))

# -------------------------------------
# print('%s' %([1, 2, 4]))

# print('%.2f' %(1.227))

#-----------------------------------
# f-string

# name = 'Trung'
# address = 'Hai duong'
# phone = '0000000'
# print(f'Student: {name}\nAddress: {address}\nPhone: {phone}')

# variable = 'Three'
# print(f'1: {{one}}, 2: {{two}}, 3: {variable}')           # 1: {one}, 2: {two}, 3: Three

#------------------------------------
# .format()

# print('1: {}, 2: {}, 3:{}'.format('one', 'two', 'three'))        # 1: one, 2: two, 3:three
# print('1: {1}, 2: {2}, 3:{0}'.format('one', 'two', 'three'))     # 1: two, 2: three, 3:one

# print('get only one value: {}'.format(4 ,5)) 			# get only one value: 4  #default: index = 0
# print('get only one value: {1}'.format(4 ,5))			# get only one value: 5

# print('get only one value: {1} {1}'.format(4 ,5))		# get only one value: 5 5
 
# Căn lề với format

center = 'I\'m {:$^11} Yeahhhhhhhhhh'.format('Trung')
left = '{:@<10}'.format('Trung')
right = '{:@>10}'.format('Trung')

print(center)
print(left)
print(right)

# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('01', 'Pham Duc Trung', 'Cam Giang')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('02', 'Vu Thi Ngoc', 'Binh Giang')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)











