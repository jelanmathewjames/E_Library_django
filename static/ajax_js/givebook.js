$('#search').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    var userid = $('#userid').val()
    if(userid==""){
      $('#warning').text("Id Field cannot be Empty")
    }
    $.ajax({
      url : '/book/givebook',
      method : 'POST',
      data :  {
        'csrfmiddlewaretoken' :csrf_token,
        'userid' : userid
      },
      dataType: 'json',
      success:(data)=>{
        if(data.success =='True'){
          window.location.replace('/book/givebook')
        }else if(data.success == 'False'){
          $('#warning').text("No User with This ID")
        }
      }
    })
})

$('#clear').click(()=>{
    $.ajax({
      url:'/book/clearuser',
      method:'GET',
      success:(data)=>{
        if(data.success == 'True'){
          window.location.replace('/book/givebook')
        }
      }
    })
})

$('#bookbtn1').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken').value
    var book1 = $('#bookid1').val()
    if(book1==''){
      $('#warning').text("Book ID field cannot be empty")
    }else{
      $.ajax({
        url:'/book/book1',
        method:'POST',
        data:{
          'csrfmiddlewaretoken':csrf_token,
          'book1':book1
        },
        dataType:'json',
        success:(data)=>{
          if(data.success == 'True'){
            window.location.replace('/book/givebook')
          }else if (data.success == 'False'){
            $('#warning').text("No book for this ID")
          }else if (data.success == 'Alreadyinhand'){
            $('#warning').text("Book is Already in Another Student")
          }
        }
      })
    }
})

$('#bookbtn2').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken').value
    var book2 = $('#bookid2').val()
    if(book2==''){
      $('#warning').text("Book ID field cannot be empty")
    }else{
      $.ajax({
        url:'/book/book2',
        method:'POST',
        data:{
          'csrfmiddlewaretoken':csrf_token,
          'book2':book2
        },
        dataType:'json',
        success:(data)=>{
          if(data.success == 'True'){
            window.location.replace('/book/givebook')
          }else if (data.success == 'False'){
            $('#warning').text("No book for this ID")
          }else if (data.success == 'Alreadyinhand'){
            $('#warning').text("Book is Already in Another Student")
          }
        }
      })
    }
})

$('#bookbtn3').click(()=>{
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken').value
    var book3 = $('#bookid3').val()
    if(book3==''){
      $('#warning').text("Book ID field cannot be empty")
    }else{
      $.ajax({
        url:'/book/book3',
        method:'POST',
        data:{
          'csrfmiddlewaretoken':csrf_token,
          'book3':book3
        },
        dataType:'json',
        success:(data)=>{
          if(data.success == 'True'){
            window.location.replace('/book/givebook')
          }else if (data.success == 'False'){
            $('#warning').text("No book for this ID")
          }else if (data.success == 'Alreadyinhand'){
            $('#warning').text("Book is Already in Another Student")
          }
        }
      })
    }
})

$('#logout').click(()=>{
    window.location.replace('/admin/adminlogout')
})

$('#home').click(()=>{
    window.location.replace('/admin/adminhome')
})