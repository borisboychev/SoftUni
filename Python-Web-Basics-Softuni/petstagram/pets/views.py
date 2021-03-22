from django.shortcuts import render, redirect

# Create your views here.
from pets.forms import CreatePetForm
from pets.models import Pet, Like


def pets_index(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, "pets/pet_list.html", context)


def see_details(request, pk):
    pet = Pet.objects.get(pk=pk)

    context = {
        'pet': pet,
    }
    return render(request, "pets/pet_detail.html", context)


def like(request, pk):
    pet = Pet.objects.get(pk=pk)
    likes = Like(test=str(pk))
    likes.pet = pet
    likes.save()
    return redirect('details', pk)


def create_pet(request):
    if request.method == "GET":
        context = {
            "form": CreatePetForm(),
        }
        return render(request, 'pets/pet_create.html', context)
    else:
        form = CreatePetForm(request.POST)

        if form.is_valid():
            pet = Pet(type=form.cleaned_data['type'],
                      name=form.cleaned_data['name'],
                      age=form.cleaned_data['age'],
                      description=form.cleaned_data['description'],
                      image_url=form.cleaned_data['image_url'])

            pet.save()

            return redirect('pets index')


def edit_pet(request):
    pass


def delete_pet(request):
    pass
