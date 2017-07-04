from django.shortcuts import render, HttpResponseRedirect
from .models import ListTest, AddPdfFileModel
from .forms import AddPdfForm

# Create your views here.
def home(request):
    render(request, 'home_field.html')

#添加列表，保存到数据库
def testlist(req):

    #写入数据库
    test = ListTest()
    test.labels = ["python", "django"]
    test.labels.append("allen")
    test.save()

    #读取数据库
    obs = ListTest.objects.all()
    for ob in obs:
        print((ob.labels))
    return HttpResponseRedirect("/")

#添加文件，保存到数据库
def addfile(req):
    if req.method == 'POST':
        form = AddPdfForm(req.POST, req.FILES)
        if not form.is_valid():
            print(form.errors)
            return HttpResponseRedirect("/")
        name = form.cleaned_data['name']
        file = form.cleaned_data['file']
        add_pdf_model = AddPdfFileModel(name=name, file=file)
        add_pdf_model.save()
        print('success')
        return render(req, 'add_file.html', {'form': AddPdfForm()})
    else:
        return render(req, 'add_file.html', {'form': AddPdfForm()})