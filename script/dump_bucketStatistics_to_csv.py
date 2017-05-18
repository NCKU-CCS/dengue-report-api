#-*- coding: big5 -*-
#-*- coding: cp950 -*-
import csv
import sys
import codecs


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
            row.append(str(getattr(obj, field.name)))
        print(row)
        writer.writerow(row[1:])


