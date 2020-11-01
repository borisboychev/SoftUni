from django.shortcuts import render, redirect

# Create your views here.
from app.forms import RecipeForm
from app.models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    context = {
        'form': RecipeForm()
    }
    if request.method == "GET":
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = Recipe(title=form.cleaned_data['title'],
                            image_url=form.cleaned_data['image_url'],
                            description=form.cleaned_data['description'],
                            ingredients=form.cleaned_data['ingredients'],
                            time=form.cleaned_data['time'])

            recipe.save()
            return redirect('index')
        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe.title = form.cleaned_data['title']
            recipe.image_url = form.cleaned_data['image_url']
            recipe.description = form.cleaned_data['description']
            recipe.ingredients = form.cleaned_data['ingredients']
            recipe.time = form.cleaned_data['time']

            recipe.save()
            return redirect('index')
        else:
            context = {
                'form': RecipeForm(instance=recipe),
            }
            return render(request, 'edit.html', context)



def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = RecipeForm(instance=recipe)

        form.fields['title'].widget.attrs['disabled'] = True
        form.fields['image_url'].widget.attrs['disabled'] = True
        form.fields['description'].widget.attrs['disabled'] = True
        form.fields['ingredients'].widget.attrs['disabled'] = True
        form.fields['time'].widget.attrs['disabled'] = True

        context = {
            'form': form,
        }

        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            'recipe': recipe,
            'ingredients': recipe.ingredients.split(', '),
        }
        return render(request, 'details.html', context)
