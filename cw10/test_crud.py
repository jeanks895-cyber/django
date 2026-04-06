import os
import sys

# Setup Django environment
sys.path.append(r'c:\Users\USER\mysite\cwday10')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
import django
django.setup()

from books.models import Book
from django.test import Client

# Delete existing
Book.objects.all().delete()

# Insert 6 books
for i in range(1, 7):
    Book.objects.create(title=f"Test Book {i}", author=f"Author {i}", year=2020+i)

c = Client()
resp = c.get('/')
content = resp.content.decode('utf-8')

print("Total books in DB:", Book.objects.count())
print("Items on page 1:", content.count("class=\"card book-item\""))
print("Has Next link:", "btn-next-page" in content)
