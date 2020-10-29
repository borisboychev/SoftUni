from django.shortcuts import redirect, render

from expenses_tracker.forms.profiles import ProfileForm
from expenses_tracker.models import Profile, Expense


def profile_index(request):
    context = {
        "profile": Profile.objects.all()[0]
    }
    return render(request, "profile.html", context)


def edit_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == "GET":
        context = {
            "form": ProfileForm(instance=profile)
        }
        return render(request, "profile-edit.html", context)
    else:
        form = ProfileForm(request.POST)

        if form.is_valid():
            profile.budget = form.cleaned_data["budget"]
            profile.first_name = form.cleaned_data["first_name"]
            profile.last_name = form.cleaned_data["last_name"]

            profile.save()
            return redirect("profile index")
        context = {
            "form": ProfileForm(instance=profile)
        }
        return render(request, "profile-edit.html", context)


def delete_profile(request):
    profile = Profile.objects.all()[0]

    if request.method == "GET":
        form = ProfileForm(instance=profile)
        form.fields["budget"].widget.attrs["disable"] = True
        form.fields["first_name"].widget.attrs["disable"] = True
        form.fields["last_name"].widget.attrs["disable"] = True
        context = {
            "form": form,
        }
        return render(request, "profile-delete.html", context)
    else:
        expenses = Expense.objects.all()
        expenses.delete()
        profile.delete()

        return redirect('index')


def create_profile(request):
    if request.method == "GET":
        context = {
            'form': ProfileForm(),
        }
        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)
