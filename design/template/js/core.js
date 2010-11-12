$(document).ready(function() {
    $("#message-list li").each(function () {
        $.jGrowl($(this).text(), {
        sticky: true,
        position: 'center',
        speed: 1000,
    });
});
