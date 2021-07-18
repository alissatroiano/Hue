    # avatar = Profile.objects.get(avatar=profile.avatar)
    
    image_path = change_avatar()
    
    if request method == 'POST':
        form =  ProfileForm(request.POST, instance=profile)
        profile.avatar.delete(save=True)
        profile.avatar.save(os.path.basename(image_path), File(open(image_path, ,"avatars")), save=True)
        
