def html(request):
    return render(request, 'test.html')

def header(request):
    pp_project_name = "@apex:project_name:var"
    print("@apex:question:var", "@apex:project_name:var")


# @apex:header:tag
h = "be himalia khosh omadi"
# @apex:end
