$(document).ready(function() {
    $('#mytable').DataTable();

    $('#create_book').click(()=>{
        window.location.replace('/bookcrud/createbook')
    })

})