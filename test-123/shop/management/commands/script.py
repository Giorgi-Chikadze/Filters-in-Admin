from django.core.management import BaseCommand
from shop.models import *
from django.contrib.contenttypes.models import ContentType
from faker import Faker
import time 
faker = Faker()
from django.db import transaction


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # category = Category(name = 'toys', description = 'about toys')
        # category.save()
        # print(category.id)
        
        # category = Category.objects.create(name='cars')
        # print(category.id)
        # start = time.time()
        # for _ in range(1000):
        #     category = Category.objects.create(name = faker.word())
        # end = time.time()
        # print(end-start)
        
        # start = time.time()
        # categories = []
        
        # for _ in range(10000):
        #     category = Category(name=faker.word())
        #     categories.append(category)
        # Category.objects.bulk_create(categories)
        # end = time.time()
        # print(end-start)
        
        
        # categories = Category.objects.filter(id__gt=500)
        
        # to_update = []
        
        # for category in categories:
        #     category.name = faker.word()
        #     to_update.append(category)
            
        # Category.objects.bulk_update(to_update, fields=['name'])
        
        # with transaction.atomic():
        #     category = Category.objects.create(name="For Jews")
        #     item = Item.objects.create(name='Gas Chamber', category=category)
        #     item = Item.objects.create(name='Soap', category=category)
        
        categories = Category.objects.all()
        item_objects = Item.objects.all()
        for category in categories:
            category.items.add(*item_objects)
        

