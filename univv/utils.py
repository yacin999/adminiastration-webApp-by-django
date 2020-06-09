import string
import random

from django.utils.text import slugify
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Creating Slugs part:____________________________________________________________________________________________________
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.prenom)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug



# def unique_slug_generator_for_module(instance, new_slug=None):
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(instance.designation)

#     Klass = instance.__class__
#     qs_exists = Klass.objects.filter(slug=slug).exists()
#     if qs_exists:
#         new_slug = "{}-{}".format(slug, instance.code)
#         return unique_slug_generator_for_module(instance, new_slug=new_slug)
#     return slug








# Generating html to pdf :
"""
the package that I used here if xhtml2pdf:
"""
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None