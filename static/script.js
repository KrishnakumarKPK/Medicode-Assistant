document.getElementById('diagnosisForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const diagnosis = document.getElementById('diagnosis').value.trim();
    const submitBtn = document.querySelector('.submit-btn');
    const resultsContainer = document.getElementById('resultsContainer');
    const messageContainer = document.getElementById('messageContainer');
    
    if (!diagnosis) {
        showMessage('Please enter a diagnosis', 'error');
        return;
    }
    
    // Show loading state
    submitBtn.classList.add('loading');
    submitBtn.textContent = 'Processing...';
    resultsContainer.style.display = 'none';
    messageContainer.style.display = 'none';
    
    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ diagnosis: diagnosis })
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const data = await response.json();
        
        // Reset button state
        submitBtn.classList.remove('loading');
        submitBtn.textContent = 'Get Codes';
        
        if (data.results.length > 0) {
            displayResults(data.results);
        } else {
            showMessage(data.message || 'No codes found', 'warning');
        }
    } catch (error) {
        console.error('Error:', error);
        submitBtn.classList.remove('loading');
        submitBtn.textContent = 'Get Codes';
        showMessage('Error processing request. Please try again.', 'error');
    }
});

function displayResults(results) {
    const resultsList = document.getElementById('resultsList');
    resultsList.innerHTML = '';
    
    results.forEach(result => {
        const card = document.createElement('div');
        card.className = 'result-card';
        
        card.innerHTML = `
            <h3>${result.condition}</h3>
            <div class="code-row">
                <span class="code-label">ICD-10 Code:</span>
                <span class="code-value">${result.icd}</span>
            </div>
            <div class="code-row">
                <span class="code-label">CPT Code:</span>
                <span class="code-value">${result.cpt}</span>
            </div>
        `;
        
        resultsList.appendChild(card);
    });
    
    document.getElementById('resultsContainer').style.display = 'block';
    document.getElementById('messageContainer').style.display = 'none';
}

function showMessage(message, type = 'warning') {
    const messageContainer = document.getElementById('messageContainer');
    const messageText = document.getElementById('messageText');
    
    messageText.textContent = message;
    messageContainer.className = 'message-container ' + type;
    messageContainer.style.display = 'block';
    document.getElementById('resultsContainer').style.display = 'none';
}
