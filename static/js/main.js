$.fn.serializeObject = function()
{

var postData = {};

var fdata = this.serializeArray();
$.each( fdata, function() {
    if(postData[this.name] !== undefined) {
        if (!postData[this.name].push) {
            postData[this.name] = [postData[this.name]];
        }
        postData[this.name].push(this.value || '');
    } else {
        postData[this.name] = this.value || '';
    }

});
return postData;

};

//# curl -i -H "Content-Type: application/json" -X POST -d '{"compfood-min":"1", "compfood-max":"10"}' http://localhost:5000/api/v1.0/query

$(function() {
    $.ajax()
    $('#constraints').submit(function(e) {
        e.preventDefault();
        resp = {}
        $('#constraints').serializeArray().forEach(function(form_obj) {
            resp[form_obj['name']] = form_obj['value'];
        })
        console.log(resp);

        var request = $.ajax({
            url: "/api/v1.0/query",
            type: "POST",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(resp),
            dataType: "json"
        });

        request.done(function(msg) {
            console.log(msg);
            // var recommendation = JSON.parse(msg)
        })
    });

});
