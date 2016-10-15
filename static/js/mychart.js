var data = {
        labels: ["Prophylactic zinc supplementation", "Vitamin A supplementation", "Complementary feeding education", "Public provision of complementary foods", "Breastfeeding promotion", "Balanced energy-protein supplementation", "Multiple micronutrient supplementation"],
        datasets: [{
            label: 'Amounts',
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(238, 41, 189, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(238, 41, 189, 1)'
            ],
            borderWidth: 1,
            data: [25, 45, 10, 50, 2, 3, 12]
        }]
    };

var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx).Bar(data);
