class comment(models, Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments'))
    username = models.Charfield(max_lenght=100)
    email = models.EmailField(max_length=200)
    body = models.Textfield()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.post.title

