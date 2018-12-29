/*
$(".side-bar").hover(function () {
        jQuery(this).addClass("active");
    },
    function () {
        jQuery(this).removeClass("active");
    });
*/

/*
$('.list-group-item').on('mouseover','> a', function(e) {
    $(this).addClass("active").siblings().removeClass("active");
});*/


$("ul li").click(function() {
    $(this).parent().children().removeClass("active");
    $(this).addClass("active");
});

