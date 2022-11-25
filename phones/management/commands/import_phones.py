import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            each_phone = list(csv.DictReader(csvfile, delimiter=';'))

            for line in each_phone:
                Phone.objects.create(
                    id=int(line['id']),
                    name=line['name'],
                    price=line['price'],
                    image=line['image'],
                    release_date=line['release_date'],
                    lte_exists=line['lte_exists'],
                    slug=slugify(line['name'])
                )
