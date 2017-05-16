# -*- coding: UTF-8 -*-
import csv
import sys
import codecs


from bucketStatistics.models import BucketStatistics


def get_model_fields(model):
    return model._meta.fields

filename = 'model.csv'
if len(sys.argv) >= 2:
    filename = sys.argv[1]

with open(filename, 'w', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    fields = get_model_fields(BucketStatistics)

    row = []
    for field in fields:
        row.append(field.name)
    writer.writerow(row)

    for obj in BucketStatistics.objects.all():
        row = []
        for field in fields:
            print('%s: %s(%s)'% ('field.name',getattr(obj, field.name), type(getattr(obj, field.name))))
            row.append(str(getattr(obj, field.name)))
        print(row)
        writer.writerow(row)


