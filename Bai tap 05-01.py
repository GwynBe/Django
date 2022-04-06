# Bài 05-01
for i in range(51):
    x = Employee(name='Name'+str(i), address='Address'+str(i))
    x.save()

#Bài 05-02
Employee.objects.last()
Customer.objects.last()
a = Customer.objects.all()
anh = a[23]
anh.name = 'Hoang Tuan Anh'
anh.save()

#Bài 05-03
# objects.create() thêm một bản ghi vào cuối database với các attribute được nhập vào
# Ví dụ:
Customer.objects.create(name='Tuan Anh', address='abc')
# objects.update() update bản ghi theo điều kiện filter
# Ví dụ:
Customer.objects.all().filter(id=53).update(contact_name='Tuan')
# objects.get_or_create() tìm trong database bản ghi với điều kiện được nhập vào, nếu không có 
# bản ghi nào thỏa mãn thì tạo bản ghi mới với điều kiện đã nhập
# Ví dụ:
Customer.objects.get_or_create(name='Tuan') 