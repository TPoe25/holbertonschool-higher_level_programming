$(document).ready(function() {
    const redHeader = $('#red_header');
    redHeader.click(function() {
        const headerElement = $('header');
        headerElement.css('color', '#FF0000');
    });
});