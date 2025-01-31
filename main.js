// Main JavaScript file for GiveTake platform

// Form Validation Utilities
const FormValidation = {
    // Initialize form validation for all forms with 'needs-validation' class
    init: function() {
        const forms = document.querySelectorAll('.needs-validation');
        forms.forEach(form => {
            form.addEventListener('submit', this.handleSubmit);
        });
    },

    // Handle form submission and validation
    handleSubmit: function(event) {
        if (!this.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        this.classList.add('was-validated');
    }
};

// Exchange Management
const ExchangeManager = {
    // Handle exchange actions (accept, decline, complete)
    handleExchange: async function(action, exchangeId) {
        try {
            const response = await fetch(`/${action}_exchange/${exchangeId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            if (response.ok) {
                window.location.reload();
            } else {
                throw new Error('Exchange action failed');
            }
        } catch (error) {
            console.error('Exchange action error:', error);
            this.showError('An error occurred while processing your request');
        }
    },

    // Show error message
    showError: function(message) {
        const alertDiv = document.createElement('div');
        alertDiv.className = 'alert alert-danger alert-dismissible fade show';
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        document.querySelector('.container').prepend(alertDiv);
    }
};

// UI Utilities
const UIUtils = {
    // Initialize tooltips
    initTooltips: function() {
        const tooltipTriggerList = [].slice.call(
            document.querySelectorAll('[data-bs-toggle="tooltip"]')
        );
        tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    },

    // Initialize popovers
    initPopovers: function() {
        const popoverTriggerList = [].slice.call(
            document.querySelectorAll('[data-bs-toggle="popover"]')
        );
        popoverTriggerList.map(function(popoverTriggerEl) {
            return new bootstrap.Popover(popoverTriggerEl);
        });
    },

    // Show confirmation modal
    showConfirmation: function(message, callback) {
        const modal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        document.getElementById('confirmationModal').querySelector('.modal-body').textContent = message;
        document.getElementById('confirmActionBtn').onclick = () => {
            modal.hide();
            callback();
        };
        modal.show();
    }
};

// Skill Input Enhancement
const SkillInput = {
    // Initialize skill input with autocomplete
    init: function() {
        const skillInput = document.getElementById('skill_required');
        if (skillInput) {
            skillInput.addEventListener('input', this.handleInput);
        }
    },

    // Handle skill input suggestions
    handleInput: function(event) {
        const input = event.target.value.toLowerCase();
        // Add skill suggestions logic here
    }
};

// Document Ready Handler
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    FormValidation.init();
    UIUtils.initTooltips();
    UIUtils.initPopovers();
    SkillInput.init();

    // Handle dynamic content loading
    const contentContainer = document.querySelector('.content-container');
    if (contentContainer) {
        contentContainer.classList.add('fade-in');
    }

    // Initialize custom scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Export modules for use in other scripts
window.GiveTake = {
    FormValidation,
    ExchangeManager,
    UIUtils,
    SkillInput
};