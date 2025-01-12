from django.core.management.base import BaseCommand
from django.db import transaction

from geonode.layers.models import Dataset

EFFECTS_FEATURE_INFO_TEMPLATE_HTML = '''
<h1>Impact ${properties.id}</h1>
<table>
    <thead>
        <tr>
            <th>Attribute</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Impact Date</td>
            <td>${properties.date}</td>
        </tr>
        <tr>
            <td>Impact Description</td>
            <td>${properties.description}</td>
        </tr>
        <tr>
            <td>Impact Damage</td>
            <td>${properties.damage}€</td>
        </tr>
        <tr>
            <td>Impact Damage Types</td>
            <td>${properties.damage_types}</td>
        </tr>
        <tr>
            <td>Flooding level</td>
            <td>${properties.flooding_level}</td>
        </tr>
        <tr>
            <td>Documents</td>
            <td>
                <a title="${properties.event_id}" href="/sea_storm_atlas/events/${properties.event_id}/effects/${properties.id}/documents/" target="_blank" rel="noopener">${properties.documents}</a>
            </td>
        </tr>
        <tr>
            <td>Event</td>
            <td>
                <a title="${properties.event_id}" href="/sea_storm_atlas/events/${properties.event_id}/" target="_blank" rel="noopener">${properties.event_id}</a>
            </td>
        </tr>
        <tr>
            <td>Event start</td>
            <td>${properties.date_start}</td>
        </tr>
        <tr>
            <td>Event end</td>
            <td>${properties.date_end}</td>
        </tr>
        <tr>
            <td>Event description</td>
            <td>${properties.date_end}</td>
        </tr>
        <tr>
            <td>Event origins</td>
            <td>${properties.origins}</td>
        </tr>
        <tr>
            <td>Coastal segment</td>
            <td>
                <a title="${properties.coastalsegment_id}" href="/sea_storm_atlas/segments/${properties.coastalsegment_id}/" target="_blank" rel="noopener">${properties.coastalsegment_id}</a>
            </td>
        </tr>
    </tbody>
</table>
'''

COAST_FEATURE_INFO_TEMPLATE_HTML = '''
<h1>Coastal segment ${properties.id}</h1>
<table>
    <thead>
        <tr>
            <th>Attribute</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ID</td>
            <td>
                <a title="${properties.id}" href="/sea_storm_atlas/segments/${properties.id}/" target="_blank" rel="noopener">${properties.id}</a>
            </td>
        </tr>
        <tr>
            <td>Region</td>
            <td>${properties.subregion}</td>
        </tr>
        <tr>
            <td>Code</td>
            <td>${properties.code}</td>
        </tr>
        <tr>
            <td>Hazard type</td>
            <td>${properties.ews_hazard_type}</td>
        </tr>
        <tr>
            <td>Forecasting service</td>
            <td>${properties.forecasting_service}</td>
        </tr>
    </tbody>
</table>
<p>
    <a href="/sea_storm_atlas/segments/${properties.id}/create-event/" target="_blank">Add a new event</a> 
</p>
'''

class Command(BaseCommand):
    '''
    This command applies a custom html feature info to the given dataset.

    The dataset MUST exist and have the same name ad declared above
    '''

    def add_arguments(self, parser):
        parser.add_argument('--coast-dataset')
        parser.add_argument('--effect-dataset')

    def handle(self, *args, **options):
        with transaction.atomic():

            ds = Dataset.objects.filter(name=options["effect_dataset"]).first()

            if not ds:
                print(f'No dataset found with name {options["effect_dataset"]}')

                return

            ds.use_featureinfo_custom_template = True
            ds.featureinfo_custom_template = EFFECTS_FEATURE_INFO_TEMPLATE_HTML
            ds.save()


            ds = Dataset.objects.filter(name=options["coast_dataset"]).first()

            if not ds:
                print(f'No dataset found with name {options["coast_dataset"]}')
                return

            ds.use_featureinfo_custom_template = True
            ds.featureinfo_custom_template = COAST_FEATURE_INFO_TEMPLATE_HTML
            ds.save()
