$(document).ready(function() {
    const addItemEl = $('#add_item');
    addItemEl.click(function() {
        const myLiElement = $('.my_list');
        myLiElement.append('<li>Item</li>');
    });
});