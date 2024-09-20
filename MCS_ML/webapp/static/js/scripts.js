document.getElementById('classification-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const logId = document.getElementById('log-id').value;
    const cpuUsage = document.getElementById('cpu-usage').value;
    const memoryUsage = document.getElementById('memory-usage').value;
    const networkActivity = document.getElementById('network-activity').value;
    const diskIo = document.getElementById('disk-io').value;
    const processCount = document.getElementById('process-count').value;

    fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            log_id: logId,  // Include log_id,Error resolved.
            cpu_usage: cpuUsage,
            memory_usage: memoryUsage,
            network_activity: networkActivity,
            disk_io: diskIo,
            process_count: processCount
        })
    })
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('classification-result');
            resultDiv.innerHTML = ''; // Clear previous results

            if (data.error) {
                resultDiv.innerHTML = `<p class="model-prediction">${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                <p class="model-prediction">RandomForest Prediction: ${data.rf_prediction}</p>
                <p class="model-prediction">GradientBoosting Prediction: ${data.gb_prediction}</p>
                <p class="model-prediction">XGBoost Prediction: ${data.xgb_prediction}</p>
                <strong class="final-result">Most Likely Prediction: ${data.final_prediction}</strong>
            `;
            }
        })
        .catch(error => console.error('Error:', error));
