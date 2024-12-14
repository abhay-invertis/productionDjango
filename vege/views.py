from django.shortcuts import render, redirect
from .models import Receipe
from django.db.utils import IntegrityError

def receipes(request):
    if request.method == 'POST':
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # Check if all required fields are provided
        if not receipe_name or not receipe_description:
            return render(request, 'receipes.html', {
                'error': 'All fields are required.',
            })

        try:
            # Attempt to create the Receipe
            Receipe.objects.create(
                receipe_name=receipe_name,
                receipe_image=receipe_image,
                receipe_description=receipe_description
            )
        except IntegrityError as e:
            # Handle IntegrityError gracefully
            return render(request, 'receipes.html', {
                'error': 'A recipe with this name already exists.' if 'unique' in str(e) else 'Database error.',
            })

        return redirect('/receipes/')  # Redirect to avoid form resubmission
  
    queryset  = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    
    
    context  = {'receipes' : queryset}
     # Fetch all recipes for GET requests
    return render(request, 'receipes.html', context )




def update_receipe(request , id):
    queryset = Receipe.objects.get(id = id) 
    if request.method == "POST":
        data = request.POST


        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

            queryset.save()
            return redirect ('/receipes/')

    
    context = {'receipe' : queryset}
    return render(request, 'update_receipes.html', context )

         
def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect ('/receipes/')
  