from django.utils.text import slugify

def _get_unique_slug(self, model_name):
    """
    def _get_unique_slug(self, model_name)
        model_name parameter should be model name.
    """
    try:
        slug = slugify(self.title)
    except AttributeError:
        slug = slugify(self.name)
    except:
        slug = slugify(self.category)
        
    unique_slug = slug
    num = 1
    while model_name.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug