from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from horses.models import Horse, Breed

class HorseList(LoginRequiredMixin, View):
    def get(self, request):
        mc = Breed.objects.count()
        al = Horse.objects.all()
        ctx = { 'breed_count': mc, 'horse_list': al }
        return render(request, 'horses/horse_list.html', ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Breed.objects.all()
        ctx = { 'breed_list': ml }
        return render(request, 'horses/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class HorseCreate(LoginRequiredMixin, CreateView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class HorseUpdate(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class HorseDelete(LoginRequiredMixin, DeleteView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')