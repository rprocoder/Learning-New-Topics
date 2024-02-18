# signals.py

from django.db.models.signals import *
from django.dispatch import receiver,Signal
from .models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # Your logic for handling user login goes here
    print(f"User {user.username} logged in.")

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    # Your logic for handling user logout goes here
    print(f"User {user.username} logged out.")




# @receiver(post_save, sender=User)
# def my_signal_handler(sender, instance,created, **kwargs):
#     # Perform actions you want when MyModel objects are saved
#     print("Sender object saved:", sender)
#     print("Instance object saved:", instance.password)
#     print("Created object saved:", created)
#     print("kwargs object saved:", kwargs)
    
    
# @receiver(pre_save, sender=User)
# def my_signal_handler(sender, instance, **kwargs):
#     # Perform actions you want when MyModel objects are saved
#     print("Sender object saved:", sender)
#     print("Instance object saved:", instance.password)
#     print("kwargs object saved:", kwargs)

    
# @receiver(post_delete, sender=User)
# def my_signal_handler(sender, instance, **kwargs):
#     # Perform actions you want when MyModel objects are saved
#     print("Sender object saved:", sender)
#     print("Instance object saved:", instance.password)
#     print("kwargs object saved:", kwargs)


rahul_signal=Signal()


@receiver(rahul_signal)
def my_signal_handler(sender, **kwargs):
    print('sender',sender,type(sender))
    custom_arg_value = kwargs.get('custom_arg')
    print("Custom signal received with argument:", custom_arg_value)
    # Add your custom signal handling logic here