immutable_var_tuple_ = 1, 2, 'a', 'b'
print(immutable_var_tuple_)
print(immutable_var_tuple_[0])  # Кортеж изменить нельзя, он относится к неизменяемым объектам
mutable_list = [1, 2, 'a', 'b', 'Modified']
print(mutable_list)
mutable_list.remove('Modified')
mutable_list.append('c')
print(mutable_list)
