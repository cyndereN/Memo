from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    topics = Topic.objects.order_by('priority')
    return render(request, 'To_do/index.html', {
        'topics': topics,
    })

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    return render(request, 'To_do/topic.html', {
        'topic': topic, 
        'entries': entries
    })

