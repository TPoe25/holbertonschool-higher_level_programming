$(document).ready(function() {
    const redHeader = $('#red_header');
    redHeader.click(function() {
        const headerElement = $('header');
        headerElement.addClass('red');
    });
});