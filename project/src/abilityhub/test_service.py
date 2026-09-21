import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abilityhub.settings')
django.setup()
from django.contrib.auth import get_user_model
from profiles.services import ProfileCreationService
User = get_user_model()
user, created = User.objects.get_or_create(username='testuser3', defaults={'email': 'test3@example.com'})
if created:
    user.set_password('testpass3')
    user.save()
print('User:', user)
cv_file = None
privacy_prefs = {}
try:
    profile = ProfileCreationService.create_profile_from_cv(user, cv_file, privacy_prefs)
    print('Profile created:', profile)
    print('Privacy settings:', profile.privacy_settings)
except Exception as e:
    print('Error:', e)
    import traceback
    traceback.print_exc()