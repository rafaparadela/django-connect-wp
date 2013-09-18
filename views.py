import xmlrpclib


@csrf_exempt
def last_post(request):
    username = 'admin'
    password = '*****'
    blog_id = 1
    try:
        host = xmlrpclib.ServerProxy('http://yourblogdomain.com/xmlrpc.php')
        entradas = host.metaWeblog.getRecentPosts(blog_id, username, password, 1)
        
        if entradas:
            title=entradas[0]['title']
            description=entradas[0]['description']
            url=entradas[0]['permaLink']
            return HttpResponse(json.dumps({'status':'ok', 'title': title, 'description': description, 'url': url}))
            
        else:
            return HttpResponse(json.dumps({'status': "error1"}))

    except:
        return HttpResponse(json.dumps({'status': "error0"}))