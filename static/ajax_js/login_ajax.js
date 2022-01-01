$('#loginbtn').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    var email = $('#email').val();
    var password = $('#password').val();
    if(email == ''){
        $('#warning').text('Email Field cannot be empty')
    }else if(password == ''){
        $('#warning').text('Password Field cannot be empty')
    }else{
        $.ajax({
            url:'login',
            method:'POST',
            data:{
                'csrfmiddlewaretoken':csrf_token,
                'email':email,
                'password':password
            },
            dataType:'json',
            success:(data)=>{
                if(data.success == 'True'){
                    window.location.replace("/")
                }else if(data.success == 'Verify'){
                    $('#warning').text('Your Email is not verified Check your E-mail.\n Verify to Log In')
                }else if(data.success == 'Email'){
                    $('#warning').text("The E-mail you entered doesn't belong \n to an account. Please check your \n E-mail and try again.")
                }else if(data.success == 'Password'){
                    $('#warning').text('Sorry, your password was incorrect. \n Please double-check your password.')
                }
            }
        })
    }
})