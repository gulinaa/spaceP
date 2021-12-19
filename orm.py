#select

# select * from products;
# Product.objects.all()

# select * from products where....;
# Product.objects.filter(...)

# select * from product where price = 10000;
# Product.objects.filter(price=10000)

# select * from products where price !=10000;
# Product.objects.filter(~Q(price=10000))
# Product.objects.exclude(price = 10000)

# select * from products where price > 10000; (<) (>=) (<=)
# Product.objects.filter(price__gt=10000)
# Product.objects.filter(price__lt=10000)
# Product.objects.filter(price__gte=10000)
# Product.objects.filter(price__gtt=10000)

# select * from products where category_id_ in ('phones', 'tv')
# Product.objects.filter(category_id__in=['phones', 'tv'])

# select * from products where price between 2000 and 5000;
# Product.objects.filter(price__range=[2000, 5000])

#like
#
# # select * from products where name like 'test';
# Product.objects.filter(name__exact = 'test')
#
# # select * from products where name ilike 'test';
# Product.objects.filter(name__iexact = 'test')


# select * from products where name like '%test%';
# Product.objects.filter(name__contains='test')

# select * from products where name ilike '%test%';
# Product.objects.filter(name__icontains='test')

# select * from products where name like 'test';
# Product.objects.filter(name__startwith = 'test%')

# select * from products where name ilike 'test';
# Product.objects.filter(name__istartwith='test%')


# select * from products where name like '%test';
# Product.objects.filter(name__endwith='%test')

# select * from products where name ilike '%test';
# Product.objects.filter(name__iendwith='%test')


#Получение одной записи
# Product.objects.get(id=1)
# select * from products where id=1


#ограничение набора полей
# select name,price from products;
# Product.objects.only('name', 'price')


# select id, description, category_id from products;
# Product.objects.defer('name', 'price')   #opposite of only


# select * from products by price;
# Product.objects.order_by('price')


# select * from products by price desc;
# Product.objects.order_by('-price')

# INSERT INTO products (name, description, price, category) VALUES ('Mi 10', 'норм телефон', '40000', 'phones')
# Product.objects.create('Mi 10', 'норм телефон', '40000', 'phones')
#

# Product.objects.bulk_create(
#     [
#         Product(...),
#         Product(...)
#     ]
# )
#
# product = Product(....)
# product.save()


# #update
#
# update products set price = 10000;
# Product.objects.update(price=10000)
#
# update products set price = 10000 where category = 'phone';
# Product.objects.filter(category='phones').update(price=10000)
#
# #обновляем один объект
#
# product = Product.objects.get(id=1)
# product.price = 20000
# product.save()
#
# # delete
# delete from products;
# Product.objects.delete()
#
# delete from products where category = 'tv';
# Product.objects.filter(category='tv').delete()

