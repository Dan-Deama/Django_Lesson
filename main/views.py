from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView
from .forms import AlunoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets,permissions
from .models import Aluno
from .serializers import AlunoSerializer

@login_required
def alunoView(request):
    alunos_list = Aluno.objects.all().filter(user=request.user)
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    print(aluno)
    return render(request, 'main/alunoID.html', {'aluno':aluno})

def deleteAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    return redirect('/')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('name', name)
        print('email', email)
        print('message', message)
    return render(request, 'main/contact.html')


# class AlunoCreateView(CreateView):
#     model = Aluno
#     form_class = AlunoForm
#     success_url = reverse_lazy('aluno-lista')
#     template_name = 'main/aluno_form.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

@login_required    
def aluno_create_view(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            return redirect(reverse('aluno-lista'))
    else:
        form = AlunoForm()

    return render(request, 'main/aluno_form.html', {'form': form})

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    success_url = reverse_lazy('aluno-lista')

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    