import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django_asgi_app = get_asgi_application()


from shop.models import *

item1  = Item.objects.create(name='Малина', price=12)
item2  = Item.objects.create(name='Малина', price=13)
item3  = Item.objects.create(name='Малина', price=14)
item4  = Item.objects.create(name='Малина', price=15)
item5  = Item.objects.create(name='Малина', price=16)
item6  = Item.objects.create(name='Малина', price=17)
item7  = Item.objects.create(name='Малина', price=18)
item8  = Item.objects.create(name='Малина', price=19)
item9  = Item.objects.create(name='Малина', price=20)
item10  = Item.objects.create(name='Малина', price=21)

item1.purchases.create(name='Aidai', age=18)
item2.purchases.create(name='Aisuluu', age=19)
item3.purchases.create(name='Altynai', age=18)
item4.purchases.create(name='Aijan', age=34)
item5.purchases.create(name='Aidana', age=33)
item6.purchases.create(name='Aliya', age=32)
item7.purchases.create(name='Alima', age=18)
item8.purchases.create(name='Aiturgan', age=18)
item9.purchases.create(name='Akmaral', age=19)
item10.purchases.create(name='Alana', age=29)
item1.purchases.create(name='Milana', age=16)
item2.purchases.create(name='Kasiet', age=25)
item3.purchases.create(name='Jannat', age=30)
item4.purchases.create(name='Aizada', age=29)
item5.purchases.create(name='Arai', age=28)
item6.purchases.create(name='Ainira', age=24)
item7.purchases.create(name='Slava', age=32)
item8.purchases.create(name='Olya', age=18)
item9.purchases.create(name='Zina', age=19)
item10.purchases.create(name='Aliman', age=22)



