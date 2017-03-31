from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    comments = post.comments.filter(active=True)
    comment_form = CommentForm(request.POST or None)
    new_comment = None

    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment
    }
    return render(request,'blog/post/detail.html', context)

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    form = EmailPostForm(request.POST or None)
    if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                                          post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'send': sent})
