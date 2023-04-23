$(document).ready(function () {
    // Set active category link 
    let urlParams = new URLSearchParams(window.location.search);
    let categoryParam = urlParams.get('category');

    if (categoryParam) {
        $('#category-links .btn').removeClass('btn-secondary').addClass('btn-outline-secondary');
        $('#all-artwork').removeClass('btn-secondary').addClass('btn-outline-secondary');
        $(`#category-links .btn[href*="${categoryParam}"]`).removeClass('btn-outline-secondary').addClass(
            'btn-secondary');
    } else {
        $('#category-links .btn[href="{% url "products" %}"]').removeClass('btn-outline-secondary')
            .addClass('btn-secondary');
        $(`#all-artwork`).removeClass('btn-outline-secondary').addClass(
            'btn-secondary');
    }

    // Handle visibility of back-to-top button

    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({
            scrollTop: 0
        }, 800);
        return false;
    });

    // Handle sorting of product list in select box
    $('#sort-selector').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    })
});