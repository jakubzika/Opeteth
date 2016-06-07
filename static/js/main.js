if (window.location.pathname == '/') {
    loadPage('index');
}
else {
    loadPage(window.location.pathname.substr(1));
}


resizeSidebar = function () {
    height = $(window).height();
    $('#menu').height(height);
};
var url;
$(document).ready(function () {
    url = window.location.pathname;
    resizeSidebar();


});

$(window).resize(resizeSidebar);

function loadPage(name) {
    $('#content').load('pages/' + name, function () {
        $(this).hide().fadeIn("slow");
    });
    //window.location.pathname=name;
    window.history.pushState("", "", '/' + name);
}
