$(document).ready(function() {
    $('#mytable').DataTable();

    $('#logout').click(()=>{
        window.location.replace('/logout')
    })

})