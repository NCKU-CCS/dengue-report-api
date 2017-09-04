#-*- coding: big5 -*-
#-*- coding: cp950 -*-
import csv
import sys
import codecs

import django
django.setup()
from bucketStatistics.models import BucketStatistics


def get_model_fields(model):
    return model._meta.fields

filename = 'model.csv'

with open(filename, 'w', encoding='big5') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    fields = get_model_fields(BucketStatistics)

    row = []
    for field in fields:
        row.append(field.name)
    writer.writerow(row[1:])

    for obj in BucketStatistics.objects.all():
        row = []
        for field in fields:
            print('%s: %s(%s)'% ('field.name',getattr(obj, field.name), type(getattr(obj, field.name))))
            if isinstance(getattr(obj, field.name), float):
                row.append('%.2f' % getattr(obj, field.name,4))
            else:
                row.append(str(getattr(obj, field.name)))
        print(row)
        writer.writerow(row[1:])


