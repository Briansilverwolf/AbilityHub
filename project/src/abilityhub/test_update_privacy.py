import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abilityhub.settings')
django.setup()
from django.contrib.auth import get_user_model
from profiles.services import ProfileCreationService
User = get_user_model()
user, created = User.objects.get_or_create(username='testuser5', defaults={'email': 'test5@example.com'})
if created:
    user.set_password('testpass5')
    user.save()
print('User:', user)
cv_file = None  # dummy
privacy_prefs = {}
try:
    profile = ProfileCreationService.create_profile_from_cv(user, cv_file, privacy_prefs)
    print('Profile created:', profile)
    print('Initial privacy settings:', profile.privacy_settings.__dict__)
except Exception as e:
    print('Error creating profile:', e)
    import traceback
    traceback.print_exc()
    exit(1)

# Now test update_profile_privacy
from profiles.services import ProfileCreationService  # re-import to get the update method
try:
    updated_profile = ProfileCreationService.update_profile_privacy(user, {'show_to_everyone': True, 'hide_contact_info': False})
    print('Updated profile:', updated_profile)
    print('Updated privacy settings:', updated_profile.privacy_settings.__dict__)
except Exception as e:
    print('Error updating privacy:', e)
    import traceback
    traceback.print_exc()