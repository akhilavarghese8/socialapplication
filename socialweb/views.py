from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView,DetailView
from socialweb.forms import UserProfileForm,LoginForm,PostForm,RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from api.models import Posts,Comments,UserProfile
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator





# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
decs=[signin_required,never_cache]

# Create your views here.

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

   

class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{form:self.form_class})

@method_decorator(decs,name="dispatch")   
class IndexView(CreateView,ListView):
    model=Posts
    form_class=PostForm
    template_name="index.html"
    success_url=reverse_lazy("index")
    context_object_name="posts"
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Posts.objects.all().order_by("-date")
    
class ProfileCreateView(CreateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile_create.html"
    success_url=reverse_lazy("index")
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class ProfileView(DetailView):
    model=UserProfile
    template_name="profile.html"
    content_object_name="profile-details"
    pk_url_kwarg="id"

class ProfileEditView(UpdateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile_edit.html"
    success_url=reverse_lazy("index")
    pk_url_kwarg="id"

    


@method_decorator(decs,name="dispatch")
class AddCommentView(View):
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("id")
        posts=Posts.objects.get(id=pid)
        usr=request.user
        cmt=request.POST.get("comment")
        Comments.objects.create(user=usr,post_name=posts,comment=cmt)
        return redirect("index")

@method_decorator(decs,name="dispatch")
class UpvoteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        cmt=Comments.objects.get(id=id)
        cmt.upvote.add(request.user)
        cmt.save()
        return redirect("index")

@method_decorator(decs,name="dispatch")
class UpvoteRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cmt=Comments.objects.get(id=id)
        cmt.upvote.remove(request.user)
        cmt.save()
        return redirect("index")

@method_decorator(decs,name="dispatch")
# class ProfileCreateView(CreateView):
#     model=UserProfile
#     form_class=UserProfileForm
#     template_name="profile-add.html"
#     success_url=reverse_lazy("index")
#     def form_valid(self,form):
#         form.instance.user=self.request.user
#         return super().form_valid(form)

@method_decorator(decs,name="dispatch")
class ProfileDetailView(TemplateView):
    template_name="profile-detail.html"

@method_decorator(decs,name="dispatch")
class ProfileUpdateView(UpdateView):
    model=UserProfile
    template_name="profile-edit.html"
    form_class=UserProfileForm
    success_url=reverse_lazy("index")
    pk_url_kwarg="id"

@method_decorator(decs,name="dispatch")
class PostLikeView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        pst=Posts.objects.get(id=id)
        pst.upvote.add(request.user)
        pst.save()
        return redirect("index")
    
@method_decorator(decs,name="dispatch")
class PostDislikeView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Posts.objects.get(id=id)
        pst.upvote.remove(request.user)
        pst.save()
        return redirect("index")




@method_decorator(decs,name="dispatch")
class PostsDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Posts.objects.get(id=id).delete()
        return redirect("index")
        
@method_decorator(decs,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    
