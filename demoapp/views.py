# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .forms import RegisterForm
# from .tasks import send_mail_task
#
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False  # Deactivate account until it's verified
#             user.save()
#
#             # Prepare email content
#             subject = "Activate Your Account"
#             message = f"Hi {user.username},\n\nPlease click the link below to activate your account:\n\n" \
#                       f"http://127.0.0.1:8000/activate/{user.id}/"
#             recipient_list = [user.email]
#
#             # Send email asynchronously
#             send_mail_task.delay()
#
#             return redirect('email_verification_sent')
#     else:
#         form = RegisterForm()
#
#     return render(request, 'demoapp/register.html', {'form': form})
#
# def email_verification_sent(request):
#     return render(request, 'demoapp/email_verification_sent.html')
#
# def activate_account(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#         user.is_active = True
#         user.save()
#         return redirect('login')
#     except User.DoesNotExist:
#         return render(request, 'demoapp/activation_failed.html')