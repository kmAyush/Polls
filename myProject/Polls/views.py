from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,redirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils import timezone

from .models import Question,Choice
from .forms import QuestionForm,ChoiceForm,DeleteNewForm

class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		"""RETURNS LAST 5 PUBLISHED QUESTIONS"""
		
		return Question.objects.all()

class DetailView(generic.DetailView):
	model=Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""EXCLUDES FUTURE QUESTIONS"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'

def results(request, question_id):
   	question = get_object_or_404(Question, pk=question_id)
   	return render(request, 'polls/results.html', {
    		'question': question
    })

def vote(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'question':question,
			'error_message':"You didn't select a choice",
	})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

class ResultsallView(generic.ListView):
	template_name='polls/resultsall.html'
	context_object_name='question_list'

	def get_queryset(self):
		"""RETURNS LAST 5 PUBLISHED QUESTIONS"""
		return Question.objects.all()

class ChoiceCreate(CreateView):
	model=Choice
	fields=['choice_text']

def questionadd(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			question= form.save(commit=False)
			question.pub_date=timezone.now()
			question.save()
			return redirect('polls:index')
	form = QuestionForm()
	return render(request, 'polls/question_form.html',{'form':form})

def choiceadd(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	if request.method == "POST":
		form = ChoiceForm(request.POST)
		if form.is_valid():
			choice= form.save(commit=False)
			choice.question=question
			choice.save()
			return redirect('polls:index')
	else:		
		form = ChoiceForm()
	return render(request, 'polls/choice_form.html',{'form':form})

def questiondelete(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	question.delete()	
	return redirect('polls:index')

def questionedit(request,question_id):
	oldquestion = get_object_or_404(Question, pk=question_id)
	if request.method == "POST":
		form=QuestionForm(request.POST)
		if form.is_valid():
			newquestion=form.save(commit=False)
			oldquestion.question_text=newquestion.question_text
			oldquestion.save()
			return redirect('polls:index')
	else:		
		form = QuestionForm()
	return render(request, 'polls/question_form.html',{'form':form})