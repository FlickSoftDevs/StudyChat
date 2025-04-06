# Import za Django zinazohitajika kwa views hizi kufanya kazi
from django.shortcuts import render, redirect  # Kutuma data kwa templates na kufanya redirects
from django.http import HttpResponse  # Kutuma response ya moja kwa moja
from django.contrib import messages  # Kutuma ujumbe mfupi kwa mtumiaji (errors, info, etc.)
from django.contrib.auth.decorators import login_required  # Kuhakikisha user ame-login kabla ya kufikia view
from django.db.models import Q  # Kutafuta kwa multiple fields kwa kutumia OR
from django.contrib.auth import authenticate, login, logout  # Functions za uthibitisho na login/logout
from .models import Room, Topic, Message, User  # Import models zako
from .forms import RoomForm, UserForm, MyUserCreationForm  # Import form zako

# View ya login page
def loginPage(request):
    page = 'login'
    
    # Kama user tayari ame-login, mpeleke home
    if request.user.is_authenticated:
        return redirect('home')

    # Kama user ametuma form ya login (POST)
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        # Jaribu kupata user mwenye email hiyo
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        # Kama authentication ni sahihi, mfanye login
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

# View ya kutoka (logout)
def logoutUser(request):
    logout(request)
    return redirect('home')

# View ya kusajili user mpya
def registerPage(request):
    form = MyUserCreationForm()

    # Kama form imewasilishwa
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)  # Mfanye login baada ya kusajiliwa
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})

# View ya homepage
def home(request):
    # Pata query ya utafutaji kama ipo
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # Tafuta rooms kwa kutumia topic, jina au maelezo
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()[0:5]  # Chukua topic 5 za mwanzo
    room_count = rooms.count()  # Idadi ya rooms zilizopatikana
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q))[0:3]  # Chukua message 3 za mwanzo zinazohusiana

    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)

# View ya kuonyesha room moja
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()  # Pata messages zote ndani ya room hii
    participants = room.participants.all()  # Pata users wote waliowahi kushiriki kwenye room

    if request.method == 'POST':
        if request.user.is_authenticated:
            # Hifadhi message mpya
            message = Message.objects.create(
                user=request.user,
                room=room,
                body=request.POST.get('body')
            )
            room.participants.add(request.user)  # Ongeza user kwenye participants
            return redirect('room', pk=room.id)
        else:
            messages.error(request, "You must be logged in to post a message.")

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)

# View ya kuonyesha profile ya user
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()  # Pata rooms alizounda
    room_messages = user.message_set.all()  # Pata messages zake
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

# View ya kuunda room mpya
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)

# View ya ku-update room iliyopo
@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    # Ruhusu tu host wa room kufanya update
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

# View ya kufuta room
@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    # Ruhusu tu host kufuta room
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

# View ya kufuta ujumbe
@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    # Ruhusu tu mtumiaji aliyepost message kuifuta
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})

# View ya kubadili profile ya mtumiaji
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

# View ya kuonyesha orodha ya topics
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

# View ya kuonyesha activities zote (messages)
def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})
