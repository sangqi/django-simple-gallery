$(document).ready(function () {
    var $grid = $('.grid').masonry({
        itemSelector: '.grid-item',
        columnWidth: '.grid-sizer',
        percentPosition: true
    })

    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout')
    })

    $('[data-toggle="tooltip"]').tooltip()
});

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
