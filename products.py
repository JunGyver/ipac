import os
import csv
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipactory.settings')
django.setup()

from tag.models import Tag

CSV_PATH_TASK = 'csv_file.csv'

with open(CSV_PATH_TASK) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    for row in data_reader:
        if row:
            Tag.objects.create(code=row[0], name=row[1], category_id=row[2], count=row[3])




'''
            Product.objects.create(name=row[0], menu_id=row[1], category_id=row[2], satisfactory=row[4], status=row[5], thumnail_image=row[6], price=row[7], discount_rate=row[8], monthPrice=row[9], installment=row[10], subtitle=row[11], creator_id=row[13], level_id=row[14] )
'''
