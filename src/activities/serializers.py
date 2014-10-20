from rest_framework import serializers

from models import Activity, Event


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
