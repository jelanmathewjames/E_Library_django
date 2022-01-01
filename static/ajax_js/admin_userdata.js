$(document).ready(function() {
    $('#mytable').DataTable();
    $('#logout').click(()=>{
      window.location.replace('/admin/adminlogout')
    })
    $('#create_user').click(()=>{
      window.location.replace('/usercrud/createuser')
    })
   
});