# Advanced Features & Security (Django)

## Custom User Model
This project uses a CustomUser model that extends AbstractUser.
Additional fields:
- date_of_birth
- profile_photo

Configured in settings using:
AUTH_USER_MODEL = 'accounts.CustomUser'

## Permissions & Groups
Custom permissions added to Blog model:
- can_view
- can_create
- can_edit
- can_delete

Groups created:
- Viewers
- Editors
- Admins

Views enforce permissions using @permission_required.
