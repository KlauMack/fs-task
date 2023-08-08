// modify visible characters of the recipe.instructions text
document.addEventListener('DOMContentLoaded', function() {
    const longTextElements = document.querySelectorAll('.long-text');
    longTextElements.forEach(function(element) {
        const maxLength = 210;
        const text = element.getAttribute('data-text');
        const truncatedText = text.length > maxLength ? text.slice(0, maxLength) + '(...)' : text;
        element.textContent = truncatedText;
    });
});
