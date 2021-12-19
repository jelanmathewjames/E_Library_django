$('#adminloginbtn').click(()=>{
    var email = $('#email').val()
    var password = $('#password').val()
    var data = {
        'csrfmiddlewaretoken':'{{csrf_token}}',
        'email':email,
        'password':password,
    }
    if(email==''){
        $('#warning').text('Email Field cannot be Empty')
    }else if(password==''){
        $('#warning').text('Password Field cannot be Empty')
    }else{
        $.ajax({
            url:'adminlogin',
            method:'POST',
            data:data,
            dataType:'json',
            success:(data)=>{
                if(data.success == 'True'){
                    window.location.replace('login')
                }else if(data.success == 'False'){
                    $('#warning').text('User Not Valid')
                }
            }
        })
    }
})



