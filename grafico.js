
const canvas = document.getElementById('meuGrafico');


const ctx = canvas.getContext('2d');


const dados = [10, 20, 30, 40, 50];


new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['A', 'B', 'C', 'D', 'E'], 
        datasets: [{
            label: 'Meu Gráfico',
            data: dados, 
            backgroundColor: 'rgba(0, 123, 255, 0.5)', 
            borderColor: 'rgba(0, 123, 255, 1)', 
            borderWidth: 1 
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true 
            }
        }
    }
});
