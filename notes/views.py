from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, NoteForm
from .models import Note
from django.http import HttpResponse



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(
        request,
        "notes/register.html",
        {"form": form}
    )

@login_required
def home(request):
    notes = Note.objects.filter(
        user=request.user
    ).order_by("execution_date")
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("home")
    else:
        form = NoteForm()
    return render(
        request,
        "notes/home.html",
        {
            "form": form,
            "notes": notes,
        }
    )

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(
        Note,
        id=note_id,
        user=request.user
    )
    if request.method == "POST":
        form = NoteForm(
            request.POST,
            instance=note
        )
        if form.is_valid():

            form.save()

            return redirect("home")
    else:
        form = NoteForm(instance=note)
    return render(
        request,
        "notes/home.html",
        {
            "form": form,
            "notes": Note.objects.filter(
                user=request.user
            ),
            "editing": True,
        }
    )

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(
        Note,
        id=note_id,
        user=request.user
    )
    if request.method == "POST":
        note.delete()
    return redirect("home")

def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/
Disallow: /login/
Disallow: /logout/
Sitemap: https://quicknote-calendar.onrender.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")