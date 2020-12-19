
var uzunluk = document.getElementById('verisay').innerHTML;

$(function(){
    for(var i=0;i<uzunluk;i++){
        $(`#myTable${i}`).dataTable()
    }
})