from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None,
                    is_active=True, is_superuser=False,
                    is_staff=False, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        user = self.model(
            email=self.normalize_email(email),
            is_active = is_active,
            is_superuser = is_superuser,
            is_staff = is_staff,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password,
                        is_active=True, is_superuser=True,
                        is_staff=True, **extra_fields):
        if is_staff is not True:
            raise ValueError("Super user must have is_staff True")
        user = self.create_user(
            email,
            password,
            is_staff=is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
            **extra_fields
        )
        user.save(using=self._db)
        return user