$('#search').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    var bookid = $('#bookid').val()
    if(bookid == ""){
      $('#warning').text("Id Field cannot be Empty")
    }
    $.ajax({
      url : '/book/returnbook',
      method : 'POST',
      data :  {
        'csrfmiddlewaretoken' :csrf_token,
        'bookid' : bookid
      },
      dataType: 'json',
      success:(data)=>{
        if(data.success =='True'){
          window.location.replace('/book/returnbook')
        }else if(data.success == 'False'){
          $('#warning').text("No User with This ID")
        }
      }
    })
})
$('#clear').click(()=>{
    $.ajax({
        url:'/book/clearbook',
        method:'GET',
        success:(data)=>{
            if(data.success == 'True'){
            window.location.replace('/book/returnbook')
            }
        }
    })
})
$('#returnbook').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    $.ajax({
      url:'/book/confirmreturn',
      method:'POST',
      data:{
        'csrfmiddlewaretoken':csrf_token,
      },
      dataType:'json',
      success:(data)=>{
        if(data.success == 'True'){
          window.location.replace('/book/returnbook')
        }
      }
    })
})
$('#logout').click(()=>{
    window.location.replace('/admin/adminlogout')
})
$('#home').click(()=>{
    window.location.replace('/admin/adminhome')
})