
@login_required
def get_title_suggestions(request):
    form = ArtworkForm()
    
    if request.method == 'POST':
        # Retrieve the artwork description from the POST request
        text = request.POST.get('text')
        # Call your MindsDB/ChatGPT model to get the predictions
        project = mdb_server.get_project('mindsdb')

        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']            z
            try:
                query = project.query(f'SELECT * FROM mindsdb.test_openai_art_3 WHERE artwork_description="{text}";')
                response = query.fetch()['predictions']
                predictions = response
                print(query.fetch())

                title_suggestions_html = '<datalist id="title-suggestions">'

                for predictions in query.fetch()['predictions']:
                    title_suggestions_html += f'<option value="{predictions}">'
                    return title_suggestions_html + '</datalist>'
            except:
                pass
        else:
            return '<datalist id="title-suggestions"></datalist>'
        
            predictions = ['', '', '']
            print(predictions)
            
    return redirect(reverse('add_product'))
