from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    DEFAULT_AVATAR = "/uploads/user_pics/default_avatar.jpg"

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, verbose_name="Пользователь")
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name="Аватар")
    about = models.TextField(max_length=3000, null=True, blank=True, verbose_name="О себе")
    github = models.URLField(null=True, blank=True, verbose_name="Профиль Github")

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Team(models.Model):
    user = models.ForeignKey(User, related_name="teams", on_delete=models.CASCADE, verbose_name='Юзер')
    project = models.ForeignKey("webapp.Project", related_name="teams", on_delete=models.CASCADE,
                                verbose_name='Проект')
    start_date = models.DateTimeField(verbose_name="Start date")
    end_date = models.DateTimeField(verbose_name="End date", null=True, blank=True)

    def __str__(self):
        return str(self.user)

