from iws.sea_storm_atlas.models import StormEventEntry, StormEventEffect, CoastalSegment, Origin, Sea, DamageCategory
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
from rest_framework import serializers


class CostalSegmentSerializer(DynamicModelSerializer):
    ews_hazard_type__name = serializers.SerializerMethodField()
    sea = DynamicRelationField('StormSeaSerializer', embed=True)

    class Meta:
        model = CoastalSegment
        fields = (
            'id',
            'region',
            'subregion',
            'sea',
            'seg_name',
            'code',
            'partition',
            'ews',
            'ews_hazard_type',
            'ews_hazard_type__name',
            'forecasting_service',
            'cp_procedures',
            'intervention_procedures',
            'cf_risk_sources',
            'network_for_marine_measurement_observation',
            'post_event_monitoring_system',
            'geom',
        )

        deferred_fields = ('geom',)

    def get_ews_hazard_type__name(self, obj):
        return obj.get_ews_hazard_type_display()


class StormEventEntrySerializer(DynamicModelSerializer):
    effects_count = serializers.SerializerMethodField()

    class Meta:
        model = StormEventEntry
        fields = (
            'id',
            'name',
            'date_start',
            'date_end',
            'description',
            'origins',
            'is_aggregated',
            'effects_count',
            'coastalsegment',
            'coastalsegment_id',
        )

    origins = DynamicRelationField('StormOriginSerializer', many=True, embed=True)
    coastalsegment = DynamicRelationField('CostalSegmentSerializer', embed=True)
    
    def get_effects_count(self, obj):
        return obj.effects.all().count()


class StormEventEffectSerializer(DynamicModelSerializer):
    lat = serializers.SerializerMethodField()
    lon = serializers.SerializerMethodField()

    class Meta:
        model = StormEventEffect
        fields = (
            'id',
            'date',
            'event',
            'damage_categories',
            'flooding_level',
            'damage',
            'description',
            'event_id',
            'lat',
            'lon',
        )

    event = DynamicRelationField('StormEventEntrySerializer', embed=True)
    damage_categories = DynamicRelationField('DamageCategorySerializer', many=True, embed=True)
    
    def get_lat(self, obj):
        if not obj.geom:
            return None
        obj.geom.transform(4326)
        return '%.6f' % obj.geom.centroid.y

    def get_lon(self, obj):
        if not obj.geom:
            return None
        obj.geom.transform(4326)
        return '%.6f' % obj.geom.centroid.x


class StormOriginSerializer(DynamicModelSerializer):
    class Meta:
        model = Origin
        fields = (
            'id',
            'name',
        )

class StormSeaSerializer(DynamicModelSerializer):
    class Meta:
        model = Sea
        fields = (
            'id',
            'label',
        )

class DamageCategorySerializer(DynamicModelSerializer):
    class Meta:
        model = DamageCategory
        fields = (
            'id',
            'name',
        )
