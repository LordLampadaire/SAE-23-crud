class comment(models, Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments'))
    username = models.Charfield(max_lenght=100)
    email = models.EmailField(max_length=200)
    body = models.Textfield()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.post.title

def post_detail(request, slug: str):
    post = get_object_or_(Post, slup=slug)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm<data=request.post>
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentFOrm()
    return render(request, "///.html", {
                                        "comments": comments,
                                        "post": post,
                                        "new_comment" : new,
                                        })
