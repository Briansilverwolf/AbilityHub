import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abilityhub.settings')
django.setup()
from django.contrib.auth import get_user_model
from profiles.services import ProfileCreationService
User = get_user_model()
user, created = User.objects.get_or_create(username='testuser4', defaults={'email': 'test4@example.com'})
if created:
    user.set_password('testpass4')
    user.save()
print('User:', user)
cv_file = None  # dummy
privacy_prefs = {}
try:
    profile = ProfileCreationService.create_profile_from_cv(user, cv_file, privacy_prefs)
    print('Profile created:', profile)
    print('Privacy settings:', profile.privacy_settings)
    print('Privacy settings ID:', profile.privacy_settings.id)
except Exception as e:
    print('Error:', e)
    import traceback
    traceback.print_exc()