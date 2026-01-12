// Sample data for testing
function fillSampleData() {
    const sampleData = {
        'Returns': 0.0125,
        'MA_7': 350.25,
        'MA_30': 345.80,
        'Volatility': 0.015,
        'Volume_Change': 0.05,
        'Close_lag_1': 349.50,
        'Close_lag_2': 347.80,
        'Close_lag_3': 346.20,
        'Close_lag_4': 345.90,
        'Close_lag_5': 344.75,
        'Close_lag_7': 343.50,
        'Day': new Date().getDate(),
        'Month': new Date().getMonth() + 1,
        'Week': new Date().getDay()
    };

    // Fill form with sample data
    Object.keys(sampleData).forEach(key => {
        const input = document.getElementById(key);
        if (input) {
            input.value = sampleData[key];
        }
    });

    // Show notification
    showNotification('Sample data loaded successfully!', 'success');
}

// Form validation
function validateForm() {
    const form = document.getElementById('predictionForm');
    let isValid = true;
    const errorMessages = [];

    // Check all required fields
    form.querySelectorAll('[required]').forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('error');
            errorMessages.push(`${input.name || input.id} is required`);
        } else {
            input.classList.remove('error');
        }
    });

    // Validate numeric ranges
    const dayInput = document.getElementById('Day');
    if (dayInput && (dayInput.value < 1 || dayInput.value > 31)) {
        isValid = false;
        dayInput.classList.add('error');
        errorMessages.push('Day must be between 1 and 31');
    }

    const monthInput = document.getElementById('Month');
    if (monthInput && (monthInput.value < 1 || monthInput.value > 12)) {
        isValid = false;
        monthInput.classList.add('error');
        errorMessages.push('Month must be between 1 and 12');
    }

    const weekInput = document.getElementById('Week');
    if (weekInput && (weekInput.value < 0 || weekInput.value > 6)) {
        isValid = false;
        weekInput.classList.add('error');
        errorMessages.push('Week day must be between 0 and 6');
    }

    if (!isValid) {
        showNotification(`Please fix the following errors:\n${errorMessages.join('\n')}`, 'error');
        return false;
    }

    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) {
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Predicting...';
        submitBtn.disabled = true;
    }

    return true;
}

