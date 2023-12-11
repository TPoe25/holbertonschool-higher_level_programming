$(document).ready(function() {
    const toggleHeadElement = $('#toggle_header');
    toggleHeadElement.click(function() {
        const headElement = $('header');
        headElement.toggleClass('red green');
    });
});