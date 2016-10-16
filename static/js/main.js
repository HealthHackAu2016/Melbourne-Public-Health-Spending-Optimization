
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

var resultobj = new Object();
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
            resultobj = JSON.parse({
    "beps": 0.320181809, 
    "bfpromo": 0.045568297, 
    "compfood": 1.262295447, 
    "edu": 24694524.49, 
    "fval": 16710300.15, 
    "micros": 1.566272582, 
    "vitA": 0.179626545, 
    "zinc": 6.837015246
  });
        });

var resultArray = [];
resultArray[0] = resultojb.zinc;
resultArray[1] = resultobj.vitA;
resultArray[2] = resultobj.edu;
resultArray[3] = resultobj.compfood;
resultArray[4] = resultobj.bfpromo;
resultArray[5] = resultobj.beps;
resultArray[6] = resultobj.micros;

var ctx = document.getElementById("myResultChart").getContext('2d');

var myChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Prophylactic zinc supplementation", "Vitamin A supplementation", "Complementary feeding education", "Public provision of complementary foods", "Breastfeeding promotion", "Balanced energy-protein supplementation", "Multiple micronutrient supplementation"],
    datasets: [{
      backgroundColor: [
        "#2ecc71",
        "#3498db",
        "#95a5a6",
        "#9b59b6",
        "#f1c40f",
        "#e74c3c",
        "#34495e"
      ],
      data: resultArray
    }]
  }
});


    });

});

//var resultData= [6.837015246, 	0.179626545, 24694524.49, 1.262295447,  0.045568297, 0.320181809, 1.566272582]

