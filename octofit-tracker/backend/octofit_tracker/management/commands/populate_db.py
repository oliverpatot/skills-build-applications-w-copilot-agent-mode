from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', team=marvel)
        steve = User.objects.create_user(username='captainamerica', email='steve@marvel.com', password='password', team=marvel)
        bruce = User.objects.create_user(username='hulk', email='bruce@marvel.com', password='password', team=marvel)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', team=dc)
        bruce_dc = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        Activity.objects.create(user=clark, type='fly', duration=120, calories=1000)
        Activity.objects.create(user=bruce_dc, type='fight', duration=90, calories=700)

        # Create Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        Workout.objects.create(name='Flight Training', description='Workout for flying heroes')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
