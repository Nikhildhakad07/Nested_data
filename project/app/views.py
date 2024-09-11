from django.shortcuts import render


# Create your views here.

'''def home(request):
    data1 = {'name':{'1st':{'name':"Nikhil",'age':35},'2nd':"Ram",'3rd':"Raj"}}
    data2 = {'name':'Nikhil','age':37,'qualification':'B.com'}
    data3 = {'name':'Nikhil','age':37,'qualification':'B.com'}
    data4 = {'name':'Nikhil','age':37,'qualification':'B.com'}
    #return render (request,'index.html',data2)
    return render(render,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4''})
    '''


from django.shortcuts import render

# Create your views here.
# def home(request):
#     data1=str()
#     data2=['neeraj',10,20]
#     return render(request,'home.html',{'key1':data1,'key2':data2})

# def home(request):
#     data1 = {'name':{'1st':{'name':"Arvind",'age':35},'2nd':"rahul",'3rd':"Raj"},'age':37,'qualification':'M.Tech'}
#     data2 = {'name':'Neeraj','age':37,'qualification':'M.Tech'}
#     data3 = {'name':'Neeraj','age':37,'qualification':'M.Tech'}
#     data4 = {'name':'Neeraj','age':37,'qualification':'M.Tech'}
#     # return render(request,'index.html',data)
#     return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data 3,'key4':data4})

# def home(request):
#     data1 = {}
#     data2 = {}
#     data3 = {}
#     data4 = {}
#     # return render(request,'index.html',data)
#     return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})

# def home(request):
#     data1 = {'name':'Neeraj'}
#     data2 = {}
#     data3 = {}
#     data4 = {}
#     # return render(request,'index.html',data)
#     return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})

def home(request):
    data1 = {'value':'From key1'}
    data2 = {}
    data3 = {}
    data4 = {}
    # return render(request,'index.html',data)
    return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})


def collection(request):

    data = [{'name':'Nikhil','age':18,'quali':'B.tech'},
            {'name':'Raj','age':23,'quali':'M.tech'},
            {'name':'Ram','age':27,'quali':'b.tech'},
            {'name':'Rajesh','age':67,'quali':'M.tech'}]
    
    return render(request,'collection.html',{'data':data})