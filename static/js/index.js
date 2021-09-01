
function observer(){
        $.ajax({
            url: "get_info",
            method: 'get',
            contentType: 'application/json',
            data: JSON.stringify({}),
            success: function(response){
                table_a = ""
                for (i = 0; i<response["data"].length; i++){
                    td = "<td>"+(i+1)+"</td><td>"+response["data"][i]+"</td>"
                    tr = "<tr>"+td+"</tr>"
                    table_a += tr
                }
                $(".table_record").html(table_a)
            },
            error: function(){
                console.log('error download')
            }
        })
   }
$(document).ready(function(){
    $.ajax({
            url: "get_info",
            method: 'get',
            contentType: 'application/json',
            data: JSON.stringify({}),
            success: function(response){
                table_a = ""
                for (i = 0; i<response["data"].length; i++){
                    td = "<td>"+(i+1)+"</td><td>"+response["data"][i]+"</td>"
                    tr = "<tr>"+td+"</tr>"
                    table_a += tr
                }
                $(".table_record").html(table_a)
            },
            error: function(){
                console.log('error download')
            }
        })
   let timer = setInterval(observer, 5000)
});
