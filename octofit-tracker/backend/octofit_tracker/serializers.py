from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
	id = serializers.CharField(source='_id', read_only=True)
	class Meta:
		model = User
		fields = ['id', 'name', 'email', 'team']

class TeamSerializer(serializers.ModelSerializer):
	id = serializers.CharField(source='_id', read_only=True)
	class Meta:
		model = Team
		fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
	id = serializers.CharField(source='_id', read_only=True)
	class Meta:
		model = Activity
		fields = ['id', 'user', 'activity', 'duration']

class WorkoutSerializer(serializers.ModelSerializer):
	id = serializers.CharField(source='_id', read_only=True)
	class Meta:
		model = Workout
		fields = ['id', 'user', 'workout', 'reps']

class LeaderboardSerializer(serializers.ModelSerializer):
	id = serializers.CharField(source='_id', read_only=True)
	class Meta:
		model = Leaderboard
		fields = ['id', 'team', 'points']
