import django
django.setup()
from bucketStatistics.models import BucketStatistics
from bucketRecord.models import BucketRecord

BucketStatistics.objects.all().delete();

BucketRecords = BucketRecord.objects.all()
village_list = []

for R in BucketRecords:
    county = R.county
    town = R.town
    village = R.village

    if([county, town, village] not in village_list):
        village_list.append([county, town, village])

for item in village_list:
    county = item[0]
    town = item[1]
    village = item[2]

    village_BucketRecords = BucketRecord.objects.filter(
            county=county
        ).filter(
            town=town
        ).filter(village=village)

    investigate_dates = []
    for record in village_BucketRecords:
        if(record.investigate_date not in investigate_dates):
            investigate_dates.append(record.investigate_date)

    for date in investigate_dates:
        date_of_village_BucketRecords = village_BucketRecords.filter(investigate_date=date)
        total_egg_count = sum(r.egg_count for r in date_of_village_BucketRecords if r.egg_count > 0)
        bucketes_has_egg = sum(r.egg_count > 0 for r in date_of_village_BucketRecords)
        positive_rate = bucketes_has_egg / len(date_of_village_BucketRecords)
        avg_egg_count = 10 * (total_egg_count / len(date_of_village_BucketRecords))

        BucketStatistics(
            investigate_date=date,
            county=county,
            town=town,
            village=village,
            total_egg_count=total_egg_count,
            positive_rate=positive_rate,
            avg_egg_count=avg_egg_count
        ).save()
