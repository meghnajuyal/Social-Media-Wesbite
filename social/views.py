from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from social.models import Profile,Comment,Post,PostLike,FollowUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from . import forms
from django.http import HttpResponseRedirect
from social.models import  Profile,Post,Comment,FollowUser,PostLike
from django.shortcuts import redirect



# Create your views here.
@method_decorator(login_required,name="dispatch")
class HomeView(TemplateView):
    template_name="social/home.html"
    def get_context_data(self,**kwargs):
        context=TemplateView.get_context_data(self,**kwargs)
        follow=FollowUser.objects.filter(followed_by=self.request.user.profile)
        followedlist=[]
        for f in follow:
            followedlist.append(f.profile)
        si=self.request.GET.get("si")
        if si==None:
            si=""

        postlist=Post.objects.filter(Q(uploaded_by__in=followedlist)).filter(Q(subject__icontains=si)|Q(msg__icontains=si)).order_by("-id")

        for p in postlist:
            p.liked=False
            ob=PostLike.objects.filter(post=p,liked_by=self.request.user.profile)
            if ob:
                p.liked=True
            ob=PostLike.objects.filter(post=p)
            comment_count=Comment.objects.filter(post=p)
            p.comment_count=comment_count.count
            p.likes=ob.count

        context["post_list"]=postlist
        return context

class AboutView(TemplateView):
    template_name="social/about.html"

class IndexView(TemplateView):
    template_name="social/index.html"


class RegisterView(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name="registration/registeration_form.html"


@method_decorator(login_required,name="dispatch")
class ProfileUpdateView(UpdateView):
    model=Profile
    fields=["name","age","gender","address","status","contact","description","pic"]
    success_url=reverse_lazy('social:home')


@method_decorator(login_required,name="dispatch")
class PostCreateView(CreateView):
    model=Post
    success_url=reverse_lazy('social:postList')
    fields=["subject","msg","pic"]

    def form_valid(self,form):
        self.object=form.save()
        self.object.uploaded_by=self.request.user.profile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required,name="dispatch")
class PostListView(TemplateView):
    template_name="social/post_list.html"
    def get_context_data(self,**kwargs):
        context=TemplateView.get_context_data(self,**kwargs)
        si=self.request.GET.get("si")
        if si==None:
            si=""

        postlist=Post.objects.filter(Q(uploaded_by=self.request.user.profile)).filter(Q(subject__icontains=si)|Q(msg__icontains=si)).order_by("-id")

        for p in postlist:
            p.liked=False
            ob=PostLike.objects.filter(post=p,liked_by=self.request.user.profile)
            if ob:
                p.liked=True
            ob=PostLike.objects.filter(post=p)
            comment_count=Comment.objects.filter(post=p)
            p.comment_count=comment_count.count
            p.likes=ob.count

        context["post_list"]=postlist
        return context









@method_decorator(login_required,name="dispatch")
class PostDetailView(DetailView):
    model=Post

@method_decorator(login_required,name="dispatch")
class PostDeleteView(DeleteView):
    model=Post
    success_url=reverse_lazy('social:postList')


@method_decorator(login_required,name="dispatch")
class ProfileListView(ListView):
    model=Profile

    def get_queryset(self):
        si=self.request.GET.get("si")
        if si==None:
            si=""

        proflist= Profile.objects.filter(~Q(user=self.request.user)).filter(Q(name__icontains=si)|Q(address__icontains=si)).order_by("-id")
        for p in proflist:
            p.followed=False
            ob=FollowUser.objects.filter(profile=p,followed_by=self.request.user.profile)
            if ob:
                p.followed=True
        return proflist

@method_decorator(login_required,name="dispatch")
class ProfileDetailView(DetailView):
    model=Profile





def follow_user(request,pk):
    user=Profile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user,followed_by=request.user.profile)

    return HttpResponseRedirect(reverse_lazy('social:profileList'))


def unfollow_user(request,pk):
    user=Profile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user,followed_by=request.user.profile).delete()

    return HttpResponseRedirect(reverse_lazy('social:profileList'))


def postlike(request,pk):
    post=Post.objects.get(pk=pk)
    PostLike.objects.create(post=post,liked_by=request.user.profile)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def postunlike(request,pk):
    post=Post.objects.get(pk=pk)
    PostLike.objects.filter(post=post,liked_by=request.user.profile).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required
def CommentAddView(request,pk):
    post=Post.objects.get(pk=pk)

    if request.method =='POST':
         form=forms.CommentForm(request.POST)

         if form.is_valid():
             comment=form.save(commit=False)
             comment.post=post
             comment.commented_by=request.user.profile

             comment.save()
             return redirect('social:postDetail',pk=post.pk)


    else:
        form=forms.CommentForm()
    return render(request,'social/comment_form.html',{'form':form})
