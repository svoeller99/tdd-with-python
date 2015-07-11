from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
  return HttpResponse("""<html>
    <title>To-Do lists</title>
    <body>
      <h1>To-Do</h1>
      <input id="id_new_item" placeholder="Enter a to-do item" type="text" />
      <table id="id_list_table">
        <tr>
          <td>1: Buy peacock feathers</td>
        </tr>
      </table>
    </body>
  </html>""")