$(document).ready(function() {
    $('#mytable').DataTable();

    $('#logout').click(()=>{
        window.location.replace('/logout')
    })
    $('#home').click(()=>{
        window.location.replace('/user/userhome')
    })

})