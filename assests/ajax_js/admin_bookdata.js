$(document).ready(function() {
    $('#mytable').DataTable();

    $('#create_book').click(()=>{
        window.location.replace('/bookcrud/createbook')
    })
    $('#home').click(()=>{
        window.location.replace('/admin/adminhome')
    })
    $('#logout').click(()=>{
        window.location.replace('/admin/adminlogout')
    })

})