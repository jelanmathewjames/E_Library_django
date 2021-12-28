$('#createuser').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var firstname = $('#firstname').val();
    var lastname = $('#lastname').val();
    var email = $('#email').val();
    var phonenumber = $('#phonenumber').val();
    var password1 = $('#password1').val();
    var password2 = $('#password2').val();
    if(firstname == ''){
        $('#warning').text('First Name Field cannot be empty')
    }else if(lastname == ''){
        $('#warning').text('Last Name Field cannot be empty')
    }else if(email == ''){
        $('#warning').text('Email Field cannot be empty')
    }else if(phonenumber.toString().length == 0){
        $('#warning').text('Phone Number Field cannot be empty')
    }else if(password1 != password2){
        $('#warning').text('Password didnot Match')
    }else if(password1 == ''){
        $('#warning').text('Password Field cannot be empty')
    }else{
        $.ajax({
            url:'createuser',
            method:'POST',
            data:{
                'csrfmiddlewaretoken':csrf_token,
                'firstname':firstname,
                'lastname':lastname,
                'email':email,
                'phonenumber':phonenumber,
                'password':password1
            },
            dataType:'json',
            success:(data)=>{
                if(data.success == 'True'){
                    window.location.replace('/usercrud/userdata')
                }else if(data.success == 'email'){
                    $('#warning').text('Email Already Exists')
                }else if(data.success == 'phone'){
                    $('#warning').text('Phone Number Already Exists')
                }
            }
        })
    }
})