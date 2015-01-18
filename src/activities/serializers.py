from rest_framework import serializers

from models import Activity, ActivityType, Event


class ActivitySerializer(serializers.ModelSerializer):
    event = serializers.ReadOnlyField(required=False, source='event.pk')

    class Meta:
        model = Activity
        fiels = ('id', 'type', 'distance', 'duration', 'weight', 'repetitions',
                'event')


class EventSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    activities = ActivitySerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'user', 'name', 'start_time', 'end_time', 'activities')
        depth = 1

    def create(self, validated_data):
        activities_data = validated_data.pop('activities')
        obj = Event.objects.create(**validated_data)
        activities = []
        for d in activities_data:
            d['event'] = obj
            activities.append(Activity(**d))
        Activity.objects.bulk_create(activities)
        return obj


class ActivityTypeSerializer(serializers.ModelSerializer):
    score_fields = serializers.SerializerMethodField()

    class Meta:
        model = ActivityType
        fields = ('id', 'name', 'description', 'score_fields')

    def get_score_fields(self, obj):
        multipliers = [
                'distance_multiplier',
                'duration_multiplier',
                'weight_multiplier',
                'repetitions_multiplier',
                ]
        return [m.split('_')[0] for m in multipliers if getattr(obj, m, None)]

    def create(self, *args, **kwargs):
        raise NotImplementedError
