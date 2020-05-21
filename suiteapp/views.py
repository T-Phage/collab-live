from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View
from .filters import *
from django.forms import formset_factory
# from .functions import handle_uploaded_file
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        siteform = SiteForm(request.POST, request.FILES)
        if siteform.is_valid():
            siteform.save()
            return redirect('suiteapp:add_site_member')
    else:
        sites = Site.objects.all()
        siteform = SiteForm()
        files = File.objects.all()
        context = {'siteform': siteform, 'sites': sites, 'files': files}
        return render(request, 'page/index.html', context)


@login_required(login_url='login')
def mysite(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        siteform = SiteForm()
        create_folder = FolderForm(request.POST)

        if create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:mysite')

        elif siteform.is_valid():
            siteform.save()
            return redirect('suiteapp:add_site_member')

        elif form.is_valid:
            form.save()
            return redirect('suiteapp:mysite')

    else:
        user = request.user
        siteform = SiteForm()
        create_folder = FolderForm(initial={'created_by': request.user, 'is_rep': False})
        form = FileForm(initial={'uploaded_by': user})
        folders = Folder.objects.filter(is_rep=False, department=None, faculty=None, created_by=request.user, main_folder=None,)
        files = File.objects.filter(department=None, faculty=None, is_rep=False,
                                    uploaded_by=request.user)  # files from database file table

        context = {'form': form, 'create_folder': create_folder, 'folders': folders,
                   'siteform': siteform, 'files': files}
        return render(request, 'page/open.html', context)


@login_required(login_url='login')
def repository(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)
        siteform = SiteForm()

        if form.is_valid():
            form.save()
            return redirect('suiteapp:repository')

        elif create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:repository')

        elif siteform.is_valid():
            siteform.save()
            return redirect('add_site_member')

    else:
        user = request.user
        form = FileForm(initial={'uploaded_by': request.user, 'is_rep': True})
        create_folder = FolderForm(initial={'created_by': user})
        siteform = SiteForm()
        files = File.objects.filter(department=None, faculty=None, is_rep=True)

        folder_form = FolderForm()
        folders = Folder.objects.filter(is_rep=True, department=None, faculty=None)
        context = {'form': form, 'folder_form': folder_form, 'siteform': siteform,
                   'create_folder': create_folder, 'folders': folders, 'files': files, }
        return render(request, 'page/repository.html', context)


@login_required(login_url='login')
def task(request):
    siteform = SiteForm(request.POST)

    if request.method == 'POST':
        if siteform.is_valid():
            siteform.save()
            return redirect('add_site_member')
    else:
        context = {'siteform': siteform, }
        return render(request, 'page/task.html', context)


# @login_required(login_url='login')
# def taskpage(request):
#     siteform = SiteForm(request.POST)
#     form = FileForm(request.POST, request.FILES)
#     taskform = TaskForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid() and taskform.is_valid():
#             taskform.save()
#             form.save()
#             return redirect('suiteapp:task')
#         # if siteform.is_valid():
#         #     siteform.save()
#         #     return redirect('suiteapp:add_site_member')

#     #     if fileform.is_valid():
#     #         fileform.save()
#     #         # if taskform.is_valid():
#     #         #     taskform.save()
#     #         return redirect('suiteapp:task')
#     else:
#         form = FileForm(initial={'is_task':True, 'uploaded_by': request.user})
#         taskform = TaskForm(request.POST)
#         context = { 'taskform':taskform, 'form':form, }
#         return render(request, 'page/taskpage.html', context)

# def taskpage(request):
#     if request.method == 'GET':
#         form = FileForm(initial={'uploaded_by': request.user, 'is_task': True})

#         context = {'form':form}
#         return render(request, 'page/taskpage.html', context)

#         # form = FileForm(request.POST, request.FILES)
#         # if form.is_valid():
#         #     form.save()
#         #     return redirect('suiteapp:task')

#     else:
#         pass

def taskpageFunc(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        taskform = TaskForm(request.POST)

        if taskform.is_valid() and form.is_valid():
            taskform.save()
            form.save()
            # if taskform.is_save():
            return redirect('suiteapp:task')

        # elif form.is_valid():
        #     form.save()
        #     return redirect('suiteapp:task')

    else:
        taskform = TaskForm()
        form = FileForm(initial={'uploaded_by': request.user, 'is_task': True, })
        context = {'form': form, 'taskform': taskform, }
        return render(request, 'page/taskpage.html', context)


@login_required(login_url='login')
def add_site_member(request, pk):
    site = Site.objects.get(site_id=pk)
    user = request.user
    SiteUserFormSet = formset_factory(SiteUserForm, extra=5)
    formset = SiteUserFormSet()
    siteuserform = SiteUserForm(initial={'site': site, 'user': user, })
    user_list = MyUser.objects.all()
    user_filter = MyUserFilter(request.GET, queryset=user_list)
    context = {'filter': user_filter, 'siteuserform': siteuserform, 'user': user,
               'formset': formset}
    return render(request, 'page/add_site_members.html', context)


# @login_required(login_url='login')
# def deleteFile(request, pk, dept):
#     file = File.objects.get(file_id=pk)
#     if request.method == 'POST':

#         if file.department == request.user.department:
#             file.delete()
#             return redirect('suiteapp:open_department', dept)
#         elif file.faculty == request.user.department.faculty:
#             file.delete()
#             return redirect('suiteapp:open_faculty', dept)
#         elif file.department is None and file.faculty is None:
#             file.delete()
#             return redirect('suiteapp:mysite')
#     else:
#         context = {'file': file}
#         return render(request, 'page/delete.html', context)


@login_required(login_url='login')
def openFolder(request, pk):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suiteapp:openFolder', pk)

        elif create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:openFolder', pk)

    else:
        folders = Folder.objects.get(folder_id=pk)

        create_folder = FolderForm(initial={'is_rep': False, 'created_by': request.user, })
        form = FileForm(initial={'uploaded_by': request.user.id, 'folder': folders})

        files = File.objects.filter(is_rep=False, department=None, faculty=None)

        open_folder = request.user
        context = {'folders': folders, 'form': form, 'create_folder': create_folder,
                   'open_folder': open_folder, }

        return render(request, 'page/open.html', context)


@login_required(login_url='login')
def openDepartment(request, pk):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('suiteapp:open_department', pk)

        elif create_folder.is_valid():
            create_folder.save()

            return redirect('suiteapp:open_department', pk)

    else:
        files = File.objects.filter(department=request.user.department)
        department = Department.objects.get(dept_id=pk)

        create_folder = FolderForm(
            initial={'is_rep': False, 'created_by': request.user, 'department': request.user.department})

        form = FileForm(initial={'department': request.user.department.dept_id, 'uploaded_by': request.user.id, })

        folders = Folder.objects.filter(is_rep=False, department=request.user.department)

        context = {'department': department, 'form': form, 'files': files,
                   'create_folder': create_folder, 'folders': folders, }
        return render(request, 'page/open.html', context)


@login_required(login_url='login')
def openFaculty(request, pk):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)

        if create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:open_faculty', pk)

        elif form.is_valid():
            form.save()
            return redirect('suiteapp:open_faculty', pk)

    else:
        faculty = Faculty.objects.get(faculty_id=pk)

        create_folder = FolderForm(initial={'is_rep': False, 'faculty': faculty, 'created_by': request.user, })
        form = FileForm(initial={'uploaded_by': request.user, 'faculty': request.user.department.faculty, })
        files = File.objects.filter(is_rep=False, faculty=request.user.department.faculty)
        folders = Folder.objects.filter(is_rep=False, faculty=request.user.department.faculty)
        context = {'faculty': faculty, 'files': files, 'form': form,
                   'create_folder': create_folder, 'folders': folders, }
        return render(request, 'page/open.html', context)


def open_folder(request, pk):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suiteapp:open_folder', pk)

        elif create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:open_folder', pk)

    else:
        folders = Folder.objects.get(folder_id=pk)

        files = File.objects.filter(folder=folders)

        create_folder = FolderForm(initial={'is_rep': False, 'created_by': request.user, 'folder_path': request.path,
                                            'main_folder': folders, })
        form = FileForm(initial={'uploaded_by': request.user.id, 'folder': folders})

        subfolders = Folder.objects.filter(main_folder=folders)

        context = {'form': form, 'create_folder': create_folder,
                   'files': files, 'subfolders': subfolders, }

        return render(request, 'page/open_folder.html', context)


def deleteFolder(request, dep, pk, name, fk):
    folder = Folder.objects.get(folder_id=pk)
    if request.method == 'POST':
        if folder.department == request.user.department:
            folder.delete()
            return redirect('suiteapp:open_department', dep)

        elif folder.faculty == request.user.department.faculty:
            folder.delete()
            return redirect('suiteapp:open_faculty', dep)

        elif folder.main_folder is not None:
            sb = Folder.objects.get(main_folder=fk)
            folder.delete()
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            return redirect('suiteapp:open_folder', fk)

        elif folder.department is None and folder.faculty is None:
            folder.delete()
            return redirect('suiteapp:mysite')
    context = {'folder': folder}
    return render(request, 'page/delete.html', context)


@login_required(login_url='login')
def deleteFile(request, dept, pk):
    file = File.objects.get(file_id=pk)
    if request.method == 'POST':

        if file.department == request.user.department:
            file.delete()
            return redirect('suiteapp:open_department', dept)

        elif file.faculty == request.user.department.faculty:
            file.delete()
            return redirect('suiteapp:open_faculty', dept)

        elif file.folder is not None:
            dept = file.folder.folder_id
            file.delete()
            return redirect('suiteapp:open_folder', dept)

        # elif file.folder is None:
        #     file.delete()
        #     return redirect('suiteapp:open_folder', dept)

        elif file.department is None and file.faculty is None and file.folder is None:
            file.delete()
            return redirect('suiteapp:mysite')
    else:
        context = {'file': file}
        return render(request, 'page/delete.html', context)


@login_required(login_url='login')
def openfile(request, pk):
    file = File.objects.get(file_id=pk)
    return render(request, 'page/doc_page.html', {'file': file})


def search(request):
    user_list = MyUser.objects.all()
    user_filter = MyUserFilter(request.GET, queryset=user_list)
    return render(request, 'page/search.html', {'filter': user_filter})


class AjaxHandlerView(View):

    def get(self, request):
        # text = request.GET.get('button_text')
        text = request.GET.get('text')
        username = request.GET.get('username')
        user = request.GET.get('user')
        name = request.GET.get('name')
        context = {'username': username, 'user': user, 'name': name, 'text': text, }

        if request.is_ajax():

            return JsonResponse(context, status=200)
            # return JsonResponse({'seconds': t}, status=200)

        kofi = "kofi"
        sl = kofi[:-1]
        user_list = MyUser.objects.all()
        user_filter = MyUserFilter(request.GET, queryset=user_list)
        context = {'filter': user_filter, 'kofi':sl,}
        return render(request, 'page/add_site_members.html', context)