from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        teams = [
            {"name": "Team Marvel"},
            {"name": "Team DC"}
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Users
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Team Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Team Marvel"},
            {"name": "Batman", "email": "batman@dc.com", "team": "Team DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "Team DC"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Activities
        activities = [
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Captain America", "activity": "Cycling", "duration": 45},
            {"user": "Batman", "activity": "Swimming", "duration": 60},
            {"user": "Wonder Woman", "activity": "Yoga", "duration": 50}
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {"user": "Iron Man", "workout": "Pushups", "reps": 100},
            {"user": "Captain America", "workout": "Situps", "reps": 80},
            {"user": "Batman", "workout": "Pullups", "reps": 60},
            {"user": "Wonder Woman", "workout": "Squats", "reps": 90}
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {"team": "Team Marvel", "points": 250},
            {"team": "Team DC", "points": 210}
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
